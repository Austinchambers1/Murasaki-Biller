import pandas as pd
import sys

df = pd.read_csv('tabs.csv')

if df.empty:
    obj = {}
    obj[sys.argv[1]] = sys.argv[2:]
    df = pd.DataFrame(obj)
    df.to_csv('tabs.csv', index=False)
else:
    df[sys.argv[1]] = sys.argv[2:]
    df.to_csv('tabs.csv', index=False)
