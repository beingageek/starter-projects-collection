"""
This script demonstrates how to create a Pandas pivot table from a dataframe consisting of transactions.
"""
import numpy as np
import pandas as pd

'''
Notes:
A transaction can be either "Add" or "Change".
A transaction is processed in two steps: Validation and Submission.
Validation is processed by "ValidatorService", and Submission is processed by "SubmitterService".
If Validation fails, the transaction is marked as Error and audit record is added for "Validation Failed" status.
If Validation succeeds, audit record is added for "Validation Complete" status, and moves to Submission.
If Submission fails, the transaction is marked as Error and audit record is added for "Submission Failed" status.
If Submission succeeds, audit record is added for "Submission Complete" and the transaction is marked as Complete.
Each transaction will have a TransactionID, TransactionDate, TransactionType, Status, and SubmittedBy.
Example - 
    TransactionID=1, 
    TransactionDate=2023-11-10, 
    TransactionType=Add, 
    Status=Validation Complete, 
    SubmittedBy=ValidatorService
'''

# Create a list of transactions.
# Odd sequenced transaction is an Add, and each even sequenced transaction is a Change.
# Odd sequenced transaction will have Validation Complete, and Submission Complete status
# Even sequenced transaction will have Validation Complete, and Submission Failed status
tx_list = []
tx_columns = ['TransactionID', 'TransactionDate', 'TransactionType', 'Status', 'SubmittedBy']
start_date = 10
for i in range(1, 11):
    tx_date = '2023-11-' + str(start_date + i)
    for j in range(10):
        tx_id = f"{i}{j}"
        tx_type = 'Add'
        tx_status = 'Submission Complete'
        if (j + 1) % 2 == 0:
            tx_type = 'Change'
            tx_status = 'Submission Failed'
        tx_list.append([tx_id, tx_date, tx_type, 'Validation Complete', 'ValidatorService'])
        tx_list.append([tx_id, tx_date, tx_type, tx_status, 'SubmitterService'])

# Add an invalid transaction with no Status value
tx_list.append([111, '2023-11-20', 'Invalid', np.nan, 'Upload Service'])

# Create a dataframe from the transaction list
df = pd.DataFrame(tx_list, columns=tx_columns)

# Print the dataframe
print(df.to_markdown())

# Create a pivot table by Status column
pivot_table = df.pivot_table(
    index='TransactionDate', columns='Status', values='TransactionID', aggfunc='count'
)

# Create a pivot table by SubmittedBy column
pivot_table_by_submitted_by = df.pivot_table(
    index='TransactionDate', columns='SubmittedBy', values='TransactionID', aggfunc='count'
)

# Fill missing values
pivot_table_by_submitted_by = pivot_table_by_submitted_by.fillna(0)

# Print the pivot tables
print(pivot_table.to_markdown())
print(pivot_table_by_submitted_by.to_markdown())

# Flip the columns and rows
flipped_table = pivot_table.transpose()

# Print the flipped table
print(flipped_table.to_markdown())
