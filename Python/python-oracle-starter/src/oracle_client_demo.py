"""
A Python script to connect to Oracle DB and fetch user data
"""
import json
from datetime import datetime, date

import oracledb


def datetime_serializer(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type %s not serializable {type(obj)}")


def main():
    """Connect to Oracle local DB and retrieve data from USER_TABLE"""
    try:
        dsn = "localhost:1521/ORCLCDB.localdomain"
        # pylint: disable=c-extension-no-member
        with oracledb.connect(user="DB_APP_USER", password="Password1",
                              dsn=dsn, encoding="UTF-8") as connection:
            # Verify connection is successful and identify version
            print("Database version:", connection.version)
            cursor = connection.cursor()

            # Delete all data from user table
            sql = "delete from USER_TABLE"
            cursor.execute(sql)

            # Insert data
            sql = "insert into USER_TABLE(USERNAME, USER_FIRST_NAME, USER_LAST_NAME, USER_MID_INIT, USER_AGE) values " \
                  "('thomson', 'Thomson', null, null, 45) "
            cursor.execute(sql)
            connection.commit()

            # Get data and print from result set
            sql = "select USERNAME, USER_FIRST_NAME, USER_LAST_NAME, USER_MID_INIT, USER_AGE from USER_TABLE"
            result_set = cursor.execute(sql)
            for result in result_set:
                print(result)
                print(f"{result[1]} - {result[4]}")

            # Get data and convert into a dictionary using column name and corresponding value
            result_set = cursor.execute("select * from USER_TABLE")
            desc = cursor.description
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                    for row in result_set]

            # Print using custom deserializer for dates
            print(json.dumps(data, default=datetime_serializer))
            # Print formatted JSON with indents and default conversion to plain string
            print(json.dumps(data, indent=4, sort_keys=False, default=str))
            print(f"{data[0].get('USER_FIRST_NAME')} - {data[0].get('USER_AGE')}")

    # pylint: disable=broad-except
    except Exception as exc:
        print("Failed", exc)

    finally:
        print("---------------\nProgram End.")


if __name__ == "__main__":
    main()
