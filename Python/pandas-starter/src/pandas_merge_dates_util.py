import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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

    # Test
    mem_data2_1 = ['220000000', '220000001', '20230101', '20230101', '343434', '87654', 'BEN0001']
    mem_data2_2 = ['220000000', '220000001', '20230102', '20230331', '343434', '87654', 'BEN0001']
    mem_data2_3 = ['220000000', '220000001', '20230401', '20230731', '343434', '87654', 'BEN0001']
    mem_data2_4 = ['220000000', '220000001', '20230801', '20231231', '343434', '87654', 'BEN0001']
    mem_data2_5 = ['220000000', '220000002', '20230101', '20230101', '343434', '87654', 'BEN0001']
    mem_data2_6 = ['220000000', '220000002', '20230102', '20230331', '343434', '87654', 'BEN0001']
    mem_data2_7 = ['220000000', '220000002', '20230401', '20230731', '343434', '87654', 'BEN0001']
    mem_data2_8 = ['220000000', '220000002', '20230801', '20231231', '343434', '87654', 'BEN0001']
    member_df = pd.DataFrame(columns=member_id_columns, data=[mem_data2_1, mem_data2_2, mem_data2_3, mem_data2_4,
                                                              mem_data2_5, mem_data2_6, mem_data2_7, mem_data2_8])
    assert 8 == len(member_df)
    member_df = merge_dates_on_same_values_alt(
        member_df, 'FamilyID', ['MemberUniqueKey', 'MemberID', 'PolicyID', 'PlanID'],
        'EffDate', 'TermDate')
    assert 2 == len(member_df)
    assert ['20231231', '20231231'] == member_df['TermDate'].tolist()


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


def get_latest_term_for_duplicated_row(current_index_loc, duplicates_df, column_name_for_value,
                                       identifier_id_val, identifier_key):
    next_duplicate_index = current_index_loc + 1
    next_identifier_id = None
    if next_duplicate_index in duplicates_df.index:
        next_identifier_id = duplicates_df.at[next_duplicate_index, identifier_key]
    if identifier_id_val == next_identifier_id:
        return get_latest_term_for_duplicated_row(next_duplicate_index, duplicates_df, column_name_for_value,
                                                  identifier_id_val, identifier_key)
    else:
        return duplicates_df.at[current_index_loc, column_name_for_value]


def merge_dates_on_same_values_alt(df_input, identifier_key, columns_to_compare, eff_dt_col, term_dt_col):
    orig_col_names = list(df_input.columns)

    cols_for_sorting = [identifier_key] + columns_to_compare + [eff_dt_col]
    df_input.drop_duplicates(cols_for_sorting, inplace=True)
    # ignore_index is important since we want to regenerate a new index after we sort the dataframe
    df_input.sort_values(by=cols_for_sorting, inplace=True, ignore_index=True)

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
    identifier_keys_merged_for_duplicates = set()
    identifier_keys_skipped_for_errors = set()
    indices_to_update = list(rows_duplicated.index)

    for i in indices_to_update:
        try:
            identifier_id = rows_duplicated.at[i, identifier_key]
            latest_term_date = get_latest_term_for_duplicated_row(
                i, rows_to_remove, term_dt_col, identifier_id, identifier_key
            )
            merged_df.at[i, term_dt_col] = latest_term_date
            identifier_keys_merged_for_duplicates.add(identifier_id)
        except Exception as exc:
            logger.error("%s: %s, %s", identifier_id, format(type(exc)), str(exc))
            identifier_keys_skipped_for_errors.add(identifier_id)
    if len(identifier_keys_merged_for_duplicates) > 0:
        logger.info("Identifier IDs merged for duplicated values: %s", identifier_keys_merged_for_duplicates)
    if len(identifier_keys_skipped_for_errors) > 0:
        logger.info("Identifier IDs skipped due to exception: %s", identifier_keys_skipped_for_errors)

    # Remove duplicated rows from original dataframe
    merged_df.drop(rows_to_remove.index, inplace=True)

    # Drop columns from the merging
    merged_df = merged_df[orig_col_names]

    return merged_df


if __name__ == "__main__":
    main()
