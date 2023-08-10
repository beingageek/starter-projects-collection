from functools import reduce

import pandas
from lxml import etree

columns = [
    'AccountID', 'PolicyID', 'MemberID', 'FirstName', 'LastName', 'DateOfBirth', 'PolicyEffDate', 'PolicyTermDate'
]
member_data = [
    ['1', '112233', '1', 'John', 'Doe', '19850413', '20230101', '20230331'],  # <Policy><Member>
    ['1', '445566', '1', 'John', 'Doe', '19850413', '20230401', '20230630'],  # <Policy><Member><Member>
    ['1', '445566', '2', 'Jane', 'Doe', '19901213', '20230401', '20230630'],
    ['1', '778899', '1', 'John', 'Doe', '19850413', '20230701', '20231231']  # <Policy><Member>
]
member_df = pandas.DataFrame(data=member_data, columns=columns)

member_dict = {
    'FirstName': ['John', 'John, Jane', 'John']
}

print(member_df.to_markdown())
print(member_df.to_xml(index=False, row_name='PolicyInformation', root_name='EnrollmentData', ))


def str_add(series):
    """
    Combine two columns from a Panda Series to form a concatenated string
    :param series:
    :return:
    """
    return reduce(lambda x, y: x + '-----' + y, series)


def add_aggregate_column(df, group_by_columns, column_to_aggregate):
    """
    Add a new column to dataframe by combining values from two columns
    :param df:
    :param group_by_columns:
    :param column_to_aggregate:
    :return:
    """
    group_by_res = df.groupby(group_by_columns).agg({column_to_aggregate: str_add})
    print(group_by_res.to_markdown())
    df['AllFirstNames'] = group_by_res[column_to_aggregate]
    print(df.to_markdown())
    return df


def df_to_custom_xml(df):
    """
    Map a dataframe to XML using a custom mapping process
    :param df:
    :return:
    """
    xml_rows = []
    unique_policy_ids = df['PolicyID'].unique().tolist()
    print(f"Unique PolicyIDs: {unique_policy_ids}")

    for policy_id in unique_policy_ids:
        df_subset = df[df['PolicyID'] == policy_id]
        print(df_subset.to_markdown())
        member_subset = df_subset.filter(['MemberID', 'FirstName', 'LastName', 'DateOfBirth'])
        member_xml = member_subset.to_xml(index=False, row_name='MemberInformation', xml_declaration=False,
                                          root_name='A', pretty_print=False)[3: -4]

        group_by_res = df_subset.groupby(['PolicyID']).agg({'FirstName': str_add})
        # group_by_res = df_subset.groupby(['PolicyID']).FirstName.agg(str_add)
        print(group_by_res.to_markdown())
        member_subset['AllFirstNames'] = group_by_res['FirstName']
        print(member_subset.to_markdown())
        # df_subset = add_aggregate_column(df_subset, ['PolicyID'], 'FirstName')

        policy_subset = df_subset.filter(['AccountID', 'PolicyID', 'PolicyEffDate', 'PolicyTermDate'])
        policy_subset.drop_duplicates(inplace=True)
        policy_xml = policy_subset.to_xml(index=False, row_name='PolicyInformation', xml_declaration=False,
                                          root_name='A', pretty_print=False)[3: -4]

        xml_data = policy_xml.replace('</PolicyInformation>', member_xml + '</PolicyInformation>')
        xml_rows.append(xml_data)
    l_xml = etree.fromstring(f"<EnrollmentData>{''.join(xml_rows)}</EnrollmentData>")
    complete_xml = (f"<?xml version='1.0' encoding='utf-8'?>\n"
                    f"{(etree.tostring(l_xml, pretty_print=True, encoding='unicode'))}")
    return complete_xml


def xml_to_df(xml):
    """
    Map XML to using Panda
    :param xml:
    """
    l_xml = etree.fromstring(xml.replace("<?xml version='1.0' encoding='utf-8'?>", "").replace("\n", ""))
    print(etree.dump(l_xml))
    df = pandas.read_xml(xml)
    print(df.to_markdown())
    df2 = pandas.read_xml(xml, xpath='/EnrollmentData/PolicyInformation/MemberInformation')
    print(df2.to_markdown())


xml_data = df_to_custom_xml(member_df)
print("Formatted custom xml_data:\n" + xml_data)

xml_to_df(xml_data)
