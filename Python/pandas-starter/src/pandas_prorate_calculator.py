import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

def main():
    print("Prorate Calculator")
    columns = ['MemberID', 'EffectiveDate', 'ExpirationDate', 'Amount']
    # Dataframe with mid-month data
    df = pd.DataFrame(data=[
        ['123', '20240101', '20240115', 200],
        ['123', '20240116', '20240131', 300],
        ['123', '20240201', '20240229', 400],
        ['456', '20240101', '20240131', 200],
        ['456', '20240201', '20240229', 400],
        ['789', '20240101', '20240110', 200],
        ['789', '20240111', '20240229', 400],
        ['1234', '20240110', '20241231', 100]
    ], columns=columns)
    print("Original:\n" + df.to_markdown(floatfmt=",.0f"))

    df['EffectiveDatetime'] = pd.to_datetime(df['EffectiveDate'], format="%Y%m%d")
    df['ExpirationDatetime'] = pd.to_datetime(df['ExpirationDate'], format="%Y%m%d")
    df['EffectiveDateAfterTermination'] = df['ExpirationDatetime'] + pd.DateOffset(days=1)

    # Step 1: Separate records starting first of month and ending in last day of month
    first_of_month = df[(df['EffectiveDatetime'].dt.day == 1) & (df['EffectiveDateAfterTermination'].dt.day == 1)]
    first_of_month = first_of_month.filter(columns)

    # Step 2: Handle records starting in mid-month
    mid_month_start = df[df['EffectiveDatetime'].dt.day != 1]
    # Split records crossing over months
    mid_month_start_no_split = mid_month_start[mid_month_start['EffectiveDatetime'].dt.month == mid_month_start['ExpirationDatetime'].dt.month]
    mid_month_start_crossover = mid_month_start[mid_month_start['EffectiveDatetime'].dt.month != mid_month_start['ExpirationDatetime'].dt.month]
    # Make a copy and set effective dates to first of next month
    mid_month_start_crossover_copy = mid_month_start_crossover.copy()
    mid_month_start_crossover_copy['EffectiveDatetime'] = mid_month_start_crossover_copy['EffectiveDatetime'] + pd.offsets.MonthBegin(0)
    mid_month_start_crossover_copy['EffectiveDate'] = mid_month_start_crossover_copy['EffectiveDatetime'].dt.strftime('%Y%m%d')
    mid_month_start_crossover_copy = mid_month_start_crossover_copy.filter(columns)     # These will be added to final output

    # Update existing records to term end of month from effective date
    mid_month_start_crossover['ExpirationDatetime'] = mid_month_start_crossover['EffectiveDatetime'] + pd.offsets.MonthEnd(0)
    mid_month_start_crossover['ExpirationDate'] = mid_month_start_crossover['ExpirationDatetime'].dt.strftime('%Y%m%d')
    mid_month_start_crossover['EffectiveDateAfterTermination'] = mid_month_start_crossover['ExpirationDatetime'] + pd.DateOffset(days=1)
    # Combine the two dataframes with mid-month start dates - ones that didn't split, ones that now terms end of month
    mid_month_start = pd.concat([mid_month_start_no_split,  mid_month_start_crossover])
    mid_month_start.sort_values(by=['MemberID', 'EffectiveDatetime'], inplace=True)

    # Step 3: Find records terminating in mid-month
    mid_month_term = df[df['EffectiveDateAfterTermination'].dt.day != 1]

    # Step 4: Merge records that start mid-month and end mid-month
    mid_month_df = pd.merge(
        mid_month_term, mid_month_start,
        left_on=['MemberID', 'EffectiveDateAfterTermination'],
        right_on=['MemberID', 'EffectiveDatetime'],
        how='left', suffixes=('', '_end')
    )

    # Find records where we have a mid-month start but there is no corresponding
    # termed records.
    subs_mid_month_term = mid_month_term['MemberID'].unique().tolist()
    mid_month_enrollments = mid_month_start[~mid_month_start['MemberID'].isin(subs_mid_month_term)]
    mid_month_enrollments['DaysCount'] = (mid_month_enrollments['ExpirationDatetime'].dt.day -
                                            mid_month_enrollments['EffectiveDatetime'].dt.day + 1)
    mid_month_enrollments['DaysInMonth'] = mid_month_enrollments['ExpirationDatetime'].dt.daysinmonth
    mid_month_enrollments['Amount'] = mid_month_enrollments['Amount'] * mid_month_enrollments['DaysCount'] / mid_month_enrollments['DaysInMonth']

    # Step 5: Calculate prorated amount
    mid_month_df['DaysInMonth'] = mid_month_df['ExpirationDatetime_end'].dt.day - mid_month_df['EffectiveDatetime'].dt.day + 1
    mid_month_df['ProratedAmount_first'] = mid_month_df['Amount'] * (mid_month_df['ExpirationDatetime'].dt.day - mid_month_df['EffectiveDatetime'].dt.day) / mid_month_df['DaysInMonth']
    mid_month_df['ProratedAmount_first'] = mid_month_df['Amount_end'] * (mid_month_df['ExpirationDatetime_end'].dt.day - mid_month_df['EffectiveDatetime_end'].dt.day) / mid_month_df['DaysInMonth']
    mid_month_df['Amount'] = mid_month_df['ProratedAmount_first'] + mid_month_df['ProratedAmount_first']
    mid_month_df['ExpirationDate'] = mid_month_df['ExpirationDate_end']
    mid_month_df = pd.concat([mid_month_df, mid_month_enrollments])
    mid_month_df = mid_month_df.filter(columns)

    # Step 6: Merge with original records that started first of month and ended last day of month, with records that started mid-month and ended mid-month
    merged_df = pd.concat([mid_month_df, mid_month_start_crossover_copy, first_of_month])
    merged_df = merged_df.round(2)
    merged_df.sort_values(by=['MemberID', 'EffectiveDate'], inplace=True)
    merged_df.reset_index(inplace=True, drop=True)
    print(merged_df.to_markdown())

    assert 8 == len(merged_df)
    records_for_id = merged_df[merged_df['MemberID'] == '123']
    assert 2 == len(records_for_id)
    assert "['123' '20240101' '20240131' 290.32]" == str(records_for_id.iloc[0].values)
    assert "['123' '20240201' '20240229' 400.0]" == str(records_for_id.iloc[1].values)

    records_for_id = merged_df[merged_df['MemberID'] == '456']
    assert 2 == len(records_for_id)
    assert "['456' '20240101' '20240131' 200.0]" == str(records_for_id.iloc[0].values)
    assert "['456' '20240201' '20240229' 400.0]" == str(records_for_id.iloc[1].values)

    records_for_id = merged_df[merged_df['MemberID'] == '789']
    assert 2 == len(records_for_id)
    assert "['789' '20240101' '20240131' 516.13]" == str(records_for_id.iloc[0].values)
    assert "['789' '20240201' '20240229' 400.0]" == str(records_for_id.iloc[1].values)

    records_for_id = merged_df[merged_df['MemberID'] == '1234']
    assert 2 == len(records_for_id)
    assert "['1234' '20240110' '20240131' 70.97]" == str(records_for_id.iloc[0].values)
    assert "['1234' '20240201' '20241231' 100.0]" == str(records_for_id.iloc[1].values)
    print("All assertions passed!")

if __name__ == "__main__":
    main()
