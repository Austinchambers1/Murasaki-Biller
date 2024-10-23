import pandas as pd

tax_rate = .115
tip = .2

df = pd.read_csv('tabs.csv')

df = df + (df * tax_rate) + (df * tip)

df.loc['total'] = df.sum(axis=0).round(2)
print(df)

df.to_csv('total_owed.csv')