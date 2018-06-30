import pandas as pd

df = pd.read_csv('1000 Sales Records.csv')
df = pd.read_csv('1000 Sales Records.csv', index_col=0)

# df.columns = ['House_Prices'] # Corresponding column name
print(df.head())

print(df.head())