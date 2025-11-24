import unittest

import numpy as np
import pandas as pd

ADDRESS_COLUMNS = [
    "SubscriberID", "MemberId", "HomeAddressLine1", "HomeAddressLine2", "ZipCode", "State"
]
BAD_ADDRESS_DATA = [
    ["1", "11", "BAD ADDRESS", "", "98001", "WA"],
    ["1", "12", "BAD ADDRESS", "", "98001", "WA"],
    ["1", "13", "BAD ADDRESS", "", "98001", "WA"],
    ["1", "14", "A GOOD PLACE #1", "", "98011", "WA"],
    ["1", "15", "A GOOD PLACE #2", "", "98012", "WA"],
    ["2", "21", "ANOTHER GOOD ADDRESS", "", "98001", "WA"]
]
GOOD_ADDRESS_DATA = [
    ["1", "", "A GOOD PLACE", "", "98001", "WA"]
]


def replace_bad_address_data(original_data, good_addresses):
    # Replace BAD ADDRESS data with GOOD ADDRESS data.
    # Match by using SubscriberID and replace addresses for all MemberIDs.
    # But if MemberIDs have a unique or a good address, keep the original
    # address for that MemberID.

    # Merge the original data with the good addresses on SubscriberID
    # Suffixes are added to distinguish between original and new address columns
    merged_df = pd.merge(
        original_data,
        good_addresses.drop(columns=["MemberId"]),
        on="SubscriberID",
        how="left",
        suffixes=("", "_new"),
    )

    # Identify rows that have a "BAD ADDRESS"
    is_bad_address = merged_df["HomeAddressLine1"] == "BAD ADDRESS"

    # Conditionally update address fields only for rows with a bad address
    for col in ["HomeAddressLine1", "HomeAddressLine2", "ZipCode", "State"]:
        merged_df[col] = np.where(
            is_bad_address, merged_df[f"{col}_new"], merged_df[col]
        )

    # Return the dataframe with the original columns
    return merged_df[original_data.columns]


def replace_bad_address_data_alternate(original_data, good_addresses):
    # Replace BAD ADDRESS data with GOOD ADDRESS data.
    # Match by using SubscriberID and replace addresses for all MemberIDs.
    # But if MemberIDs have a unique or a good address, keep the original
    # address for that MemberID.
    good_addresses.drop(columns=["MemberId"], inplace=True)
    member_update_mask = original_data['HomeAddressLine1'] == 'BAD ADDRESS'
    skipped_members = original_data[~member_update_mask]
    original_data = original_data[member_update_mask]

    # Merge the original data with the good addresses on SubscriberID
    # Suffixes are added to distinguish between original and new address columns
    merged_df = pd.merge(
        original_data,
        good_addresses,
        on="SubscriberID",
        how="left",
        suffixes=("", "_new"),
    )
    for col in merged_df.columns:
        if col.endswith("_new"):
            original_col = col[:-4]
            merged_df[original_col] = merged_df[col]

    merged_df = merged_df.filter(original_data.columns)
    original_data = pd.concat([merged_df, skipped_members])
    original_data.sort_values(by=['SubscriberID', 'MemberId'])
    return original_data


original_df = pd.DataFrame(columns=ADDRESS_COLUMNS, data=BAD_ADDRESS_DATA)
good_addresses_df = pd.DataFrame(columns=ADDRESS_COLUMNS, data=GOOD_ADDRESS_DATA)
# fixed_df = replace_bad_address_data(original_df, good_addresses_df)
fixed_df = replace_bad_address_data_alternate(original_df, good_addresses_df)


class Test(unittest.TestCase):
    def test_one(self):
        one_data = fixed_df[fixed_df["SubscriberID"] == "1"]
        self.assertEqual(len(one_data), 5)

        # Verify the full record for the first updated address
        expected_row_0 = ["1", "11", "A GOOD PLACE", "", "98001", "WA"]
        self.assertListEqual(one_data.iloc[0].to_list(), expected_row_0)

        # Verify the full record for the second updated address
        expected_row_1 = ["1", "12", "A GOOD PLACE", "", "98001", "WA"]
        self.assertListEqual(one_data.iloc[1].to_list(), expected_row_1)

        # Verify the full record for the other updated address
        expected_row_2 = ["1", "13", "A GOOD PLACE", "", "98001", "WA"]
        self.assertListEqual(one_data.iloc[2].to_list(), expected_row_2)

        # Verify the other records remain unchanged
        expected_row_3 = ["1", "14", "A GOOD PLACE #1", "", "98011", "WA"]
        self.assertListEqual(one_data.iloc[3].to_list(), expected_row_3)

        # Verify the other records remain unchanged
        expected_row_4 = ["1", "15", "A GOOD PLACE #2", "", "98012", "WA"]
        self.assertListEqual(one_data.iloc[4].to_list(), expected_row_4)

    def test_two(self):
        two_data = fixed_df[fixed_df["SubscriberID"] == "2"]
        self.assertEqual(len(two_data), 1)

        # Verify the full record for SubscriberID "2"
        expected_row = ["2", "21", "ANOTHER GOOD ADDRESS", "", "98001", "WA"]
        self.assertListEqual(two_data.iloc[0].to_list(), expected_row)
