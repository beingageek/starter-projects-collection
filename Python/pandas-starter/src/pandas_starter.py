"""
Python script to demonstrate the usage of Pandas Library
"""
import string

import pandas as pd


def main():
    # pylint: disable=too-many-locals, too-many-statements
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
    print("-------------------------------")

    # Using objects
    pers1 = Person("George", "Foreman", 60, 1)
    pers2 = Person("George", "Foreman", 40, 2)
    pers3 = Person("George", "Foreman", 20, 3)
    pers4 = Person("George", "Foreman", 19, 4)
    persons = [pers1.__data__(), pers2.__data__(), pers3.__data__(), pers4.__data__()]
    persons_df = pd.DataFrame(persons, columns=['FirstName', 'LastName', 'Age', 'PID'])
    pers_gender_rec1 = PersonGenderRec("M", 1)
    pers_gender_rec2 = PersonGenderRec("M", 2)
    pers_gender_rec3 = PersonGenderRec("M", 3)
    pers_gender_rec5 = PersonGenderRec("M", 5)
    person_gender_records = [pers_gender_rec1.__data__(), pers_gender_rec2.__data__(),
                             pers_gender_rec3.__data__(), pers_gender_rec5.__data__()]
    person_gender_df = pd.DataFrame(person_gender_records, columns=['Gender', 'PID'])
    print("Persons:")
    print(persons_df.to_string(index=False))
    print("-------------------------------")
    print("GenderRecords:")
    print(person_gender_df.to_string(index=False))
    print("-------------------------------")

    # Left join
    pers_records = persons_df.merge(person_gender_df, on='PID', how='left')
    print("PersonRecords Left Join:")
    print(pers_records.to_string(index=False))
    print("-------------------------------")

    # Right join
    pers_records2 = persons_df.merge(person_gender_df, on='PID', how='right')
    print("PersonRecords Right Join:")
    print(pers_records2.to_string(index=False))
    print("-------------------------------")

    # Using dictionaries
    persons_dict = {pers1.pid: pers1.__json__(), pers2.pid: pers2.__json__(),
                    pers3.pid: pers3.__json__(), pers4.pid: pers4.__json__()}
    persons_df = pd.DataFrame.from_dict(persons_dict, orient='index')
    person_genders_dict = {pers_gender_rec1.pid: pers_gender_rec1.__json__(),
                           pers_gender_rec2.pid: pers_gender_rec2.__json__(),
                           pers_gender_rec3.pid: pers_gender_rec3.__json__(),
                           pers_gender_rec5.pid: pers_gender_rec5.__json__()}
    person_gender_df = pd.DataFrame.from_dict(person_genders_dict, orient='index')
    print("Persons:")
    print(persons_df.to_string())
    print("-------------------------------")
    print("GenderRecords:")
    print(person_gender_df.to_string())
    print("-------------------------------")
    pers_records3 = persons_df.join(person_gender_df)
    print("PersonRecords Joined:")
    print(pers_records3.to_string(index=False))


class Person:
    """Class to hold a person's first name, last name and age with index"""
    def __init__(self, f_name, l_name, age, pid):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.pid = pid

    def __str__(self):
        return f"{self.f_name, self.l_name, self.age, self.pid}"

    def __data__(self):
        return [self.f_name, self.l_name, self.age, self.pid]

    def __json__(self):
        return {"f_name": self.f_name, "l_name": self.l_name,
                "age": self.age}


class PersonGenderRec:
    """Class to hold a person's gender along with index"""
    def __init__(self, gender, pid):
        self.gender = gender
        self.pid = pid

    def __data__(self):
        return [self.gender, self.pid]

    def __json__(self):
        return {"gender": self.gender}


if __name__ == "__main__":
    main()
