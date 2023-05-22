import numpy as np
import pandas as pd


def main():
    member_id_columns = ['FamilyID', 'MemberUniqueKey', 'EffDate', 'TermDate', 'MemberID', 'PolicyID', 'PlanID']
    mem_data_1 = ['210000000', '211000001', '20220101', '20221231', '111111', '87654', 'BEN0001']
    mem_data_2 = ['210000000', '211000002', '20220101', '20220430', '222222', '87654', 'BEN0001']
    mem_data_3 = ['210000000', '211000002', '20220501', '20221231', '222222', '87654', 'BEN0001']
    mem_data_4 = ['210000000', '211000003', '20220501', '20221231', '333333', '87654', 'BEN0001']
    member_df = pd.DataFrame(columns=member_id_columns, data=[mem_data_1, mem_data_2, mem_data_3, mem_data_4])

    financial_columns = ['FamilyID', 'FamilyCredit', 'TotalPremium', 'BalanceAmount', 'SharedCredit',
                         'EffDate', 'TermDate']
    financial_data_1 = ['210000000', '100', '110', '0', '10', '20220101', '20220430']
    financial_data_2 = ['210000000', '100', '110', '0', '10', '20220501', '20221231']
    financial_df = pd.DataFrame(columns=financial_columns, data=[financial_data_1, financial_data_2])

    assert 4 == len(member_df)
    member_df = merge_dates_on_same_values_alt(
        member_df, 'FamilyID', ['MemberUniqueKey', 'MemberID', 'PolicyID', 'PlanID'],
        'EffDate', 'TermDate')
    assert 3 == len(member_df)
    assert ['20221231', '20221231', '20221231'] == member_df['TermDate'].tolist()

    # Change values with a different MemberID, changed from 222222 to 222444 effective 5/1
    mem_data_3 = ['210000000', '211000002', '20220501', '20221231', '222444', '87654', 'BEN0001']
    member_df = pd.DataFrame(columns=member_id_columns, data=[mem_data_1, mem_data_2, mem_data_3, mem_data_4])
    assert 4 == len(member_df)
    member_df = merge_dates_on_same_values_alt(
        member_df, 'FamilyID', ['MemberUniqueKey', 'MemberID', 'PolicyID', 'PlanID'],
        'EffDate', 'TermDate')
    assert 4 == len(member_df)
    assert ['20221231', '20220430', '20221231', '20221231'] == member_df['TermDate'].tolist()

    assert 2 == len(financial_df)
    financial_df = merge_dates_on_same_values_alt(
        financial_df, 'FamilyID', ['FamilyCredit', 'TotalPremium', 'BalanceAmount', 'SharedCredit'],
        'EffDate', 'TermDate')
    assert 1 == len(financial_df)
    assert ['20221231'] == financial_df['TermDate'].tolist()

    # Change values with a different SharedCredit
    financial_data_2 = ['210000000', '100', '110', '0', '20', '20220501', '20221231']
    financial_df = pd.DataFrame(columns=financial_columns, data=[financial_data_1, financial_data_2])
    assert 2 == len(financial_df)
    financial_df = merge_dates_on_same_values_alt(
        financial_df, 'FamilyID', ['FamilyCredit', 'TotalPremium', 'BalanceAmount', 'SharedCredit'],
        'EffDate', 'TermDate')
    assert 2 == len(financial_df)
    assert ['20220430', '20221231'] == financial_df['TermDate'].tolist()


def merge_dates_on_same_values(df_input, identifier_key, columns_to_compare, eff_dt_col, term_dt_col):
    orig_col_names = list(df_input.columns)
    df_input['eff_dt_formatted'] = pd.to_datetime(df_input[eff_dt_col])
    df_input['term_dt_formatted'] = pd.to_datetime(df_input[term_dt_col])
    df_input['eff_dt_after_term_formatted'] = df_input['term_dt_formatted'] + pd.Timedelta(days=1)
    merged_df = df_input.merge(
        df_input,
        how='left',
        left_on=[identifier_key, 'eff_dt_after_term_formatted'] + columns_to_compare,
        right_on=[identifier_key, 'eff_dt_formatted'] + columns_to_compare,
        suffixes=['', '_cal']
    )
    rows_duplicated = merged_df[merged_df['TermDate_cal'].notna()]
    rows_to_remove = df_input.reset_index().merge(
        rows_duplicated,
        how='inner',
        left_on=[identifier_key, eff_dt_col] + columns_to_compare,
        right_on=[identifier_key, eff_dt_col + '_cal'] + columns_to_compare,
        suffixes=['', '_dupe']
    ).set_index('index')
    # print("df_input:\n" + df_input.to_markdown())
    # print("merged_df:\n" + merged_df.to_markdown())
    # print("rows_duplicated:\n" + rows_duplicated.to_markdown())
    # print("rows_to_remove:\n" + rows_to_remove.to_markdown())

    # Updates TermDate where records are duplicated
    merged_df[term_dt_col] = np.where(
        merged_df['TermDate_cal'].notna(),
        merged_df['TermDate_cal'],
        merged_df[term_dt_col]
    )

    # Remove duplicated rows from original dataframe
    merged_df.drop(rows_to_remove.index, inplace=True)

    # Drop columns from the merging
    merged_df = merged_df[orig_col_names]

    # An alternative way to drop columns that were added during merge
    # cols_to_drop = [c for c in merged_df.columns
    #                 if (c.lower().endswith('_cal') or c.lower().endswith('_dupe')
    #                     or c.lower().endswith('_formatted'))]
    # merged_df.drop(cols_to_drop, axis=1, inplace=True)
    # print("merged_df:\n" + merged_df.to_markdown())
    return merged_df


def merge_dates_on_same_values_alt(df_input, identifier_key, columns_to_compare, eff_dt_col, term_dt_col):
    orig_col_names = list(df_input.columns)
    # Convert the term_dt_col string values to datetime object, add one day, and then reformat as string
    df_input['eff_dt_after_term'] = \
        (pd.to_datetime(df_input[term_dt_col]) + pd.Timedelta(days=1)).dt.strftime('%Y%m%d')
    merged_df = df_input.merge(
        df_input,
        how='left',
        left_on=[identifier_key, 'eff_dt_after_term'] + columns_to_compare,
        right_on=[identifier_key, eff_dt_col] + columns_to_compare,
        suffixes=['', '_cal']
    )
    rows_duplicated = merged_df[merged_df['TermDate_cal'].notna()]
    rows_to_remove = df_input.reset_index().merge(
        rows_duplicated,
        how='inner',
        left_on=[identifier_key, eff_dt_col] + columns_to_compare,
        right_on=[identifier_key, eff_dt_col + '_cal'] + columns_to_compare,
        suffixes=['', '_dupe']
    ).set_index('index')
    # print("df_input:\n" + df_input.to_markdown())
    # print("merged_df:\n" + merged_df.to_markdown())
    # print("rows_duplicated:\n" + rows_duplicated.to_markdown())
    # print("rows_to_remove:\n" + rows_to_remove.to_markdown())

    # Updates TermDate where records are duplicated
    merged_df[term_dt_col] = np.where(
        merged_df['TermDate_cal'].notna(),
        merged_df['TermDate_cal'],
        merged_df[term_dt_col]
    )

    # Remove duplicated rows from original dataframe
    merged_df.drop(rows_to_remove.index, inplace=True)

    # Drop columns from the merging
    merged_df = merged_df[orig_col_names]

    return merged_df


if __name__ == "__main__":
    main()
