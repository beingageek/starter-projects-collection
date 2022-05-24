"""
Python script to demonstrate the usage of Pandas Library
"""
import string

import pandas as pd


def main():
    """
    Create dataframes, manipulate and merge with another
    """
    print("Dataframe from numbers...")
    # Create a list of numbers to represent alphabets
    numbers = range(0, 26)
    # Create a dataframe from the numbers list
    dataframe_numbers = pd.DataFrame(numbers, columns=["Numbers"])
    # Print numbers in comma separated format
    print(",".join(str(e) for e in numbers))
    # Print the dataframe
    print(dataframe_numbers)
    print("-------------------------------")

    print("Dataframe from alphabets...")
    # Create a list of ASCII alphabets
    alphabets = list(string.ascii_uppercase)
    # Create a dataframe from the alphabets list
    dataframe_alphabets = pd.DataFrame(alphabets, columns=["Alphabets"])
    # Print alphabets in comma separated format
    print(",".join(alphabets))
    # Print the dataframe
    print(dataframe_alphabets)
    print("-------------------------------")

    print("Update numbers with new incremented values...")
    # Increment all numbers by 1
    dataframe_numbers.loc[dataframe_numbers['Numbers']] += 1
    print(dataframe_numbers)
    print("-------------------------------")

    print("Merge two dataframes...")
    # Convert numbers dataframe into str
    dataframe_numbers['Numbers'] = dataframe_numbers['Numbers'].astype(str)
    # Add new column from alphabets
    merged_df = dataframe_numbers.join(dataframe_alphabets)
    print(merged_df.to_string(index=False))
    print("-------------------------------")

    # Print columns as a list
    numbers_list = merged_df['Numbers'].tolist()
    print("Numbers: " + " ".join(numbers_list))
    print("Alphabets: " + "".join(merged_df['Alphabets'].tolist()))


if __name__ == "__main__":
    main()
