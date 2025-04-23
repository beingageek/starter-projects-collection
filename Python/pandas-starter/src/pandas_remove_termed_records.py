import pandas

columns = [
    'OwnerID', 'RecordID', 'EffectiveDate', 'TerminationDate', 'IsActive'
]
data = [
    [1, 11, '20250101', '20251231', 'Y'],
    [2, 22, '20250101', '20251231', 'Y'],
    [3, 33, '20250101', '20250101', 'N'],
    [1, 12, '20250101', '20250101', 'N'],
    [2, 22, '20250201', '20250201', 'N']
]

df = pandas.DataFrame(data=data, columns=columns)

print(df.to_markdown())

def remove_termed_never_effective(df):
    active_accounts = df[df['IsActive'] == 'Y']
    termed_accounts = df[df['IsActive'] != 'Y']
    termed_for_period = termed_accounts[
        termed_accounts['EffectiveDate'] != termed_accounts['TerminationDate']
    ]
    termed_same_day = termed_accounts[
        termed_accounts['EffectiveDate'] == termed_accounts['TerminationDate']
    ]
    termed_same_day_owners = termed_same_day['OwnerID'].unique().tolist()
    active_owners = active_accounts['OwnerID'].unique().tolist()
    accounts_to_keep = [i for i in termed_same_day_owners if i not in active_owners]
    # print(accounts_to_keep)
    termed_same_day = termed_same_day[termed_same_day['OwnerID'].isin(accounts_to_keep)]
    merged = pandas.concat([active_accounts, termed_for_period, termed_same_day])
    merged.sort_values(by=['OwnerID', 'RecordID'])
    return merged

df = remove_termed_never_effective(df)
print(df.to_markdown())
