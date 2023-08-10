import pandas
from lxml import etree

columns = [
    'AccountID', 'PolicyID', 'MemberID', 'FirstName', 'LastName', 'DateOfBirth', 'PolicyEffDate', 'PolicyTermDate'
]
member_data = [
    ['1', '112233', '1', 'John', 'Doe', '19850413', '20230101', '20230331'],
    ['1', '445566', '1', 'John', 'Doe', '19850413', '20230401', '20230630'],
    ['1', '445566', '2', 'Jane', 'Doe', '19901213', '20230401', '20230630'],
    ['1', '778899', '1', 'John', 'Doe', '19850413', '20230701', '20231231']
]
member_df = pandas.DataFrame(data=member_data, columns=columns)

print(member_df.to_markdown())
print(member_df.to_xml(index=False, row_name='PolicyInformation', root_name='EnrollmentData', ))


def df_to_custom_xml(df):
    xml_rows = []
    unique_policy_ids = df['PolicyID'].unique().tolist()
    print(f"Unique PolicyIDs: {unique_policy_ids}")

    for policy_id in unique_policy_ids:
        df_subset = df[df['PolicyID'] == policy_id]
        print(df_subset.to_markdown())
        member_subset = df_subset.filter(['MemberID', 'FirstName', 'LastName', 'DateOfBirth'])
        member_xml = member_subset.to_xml(index=False, row_name='MemberInformation', xml_declaration=False,
                                          root_name='A', pretty_print=False)[3: -4]
        policy_subset = df_subset.filter(['AccountID', 'PolicyID', 'PolicyEffDate', 'PolicyTermDate'])
        policy_subset.drop_duplicates(inplace=True)
        policy_xml = policy_subset.to_xml(index=False, row_name='PolicyInformation', xml_declaration=False,
                                          root_name='A', pretty_print=False)[3: -4]
        xml_data = policy_xml.replace('</PolicyInformation>', member_xml + '</PolicyInformation>')
        xml_rows.append(xml_data)
    l_xml = etree.fromstring(f"<EnrollmentData>{''.join(xml_rows)}</EnrollmentData>")
    complete_xml = (f"<?xml version='1.0' encoding='utf-8'?>\n"
                    f"{(etree.tostring(l_xml, pretty_print=True, encoding='unicode'))}")
    print(complete_xml)


df_to_custom_xml(member_df)
