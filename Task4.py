import pandas as pd

df = pd.read_csv('cleaned_phone_usage_india.csv')

print("Data Types:\n", df.dtypes)
print("\nUnique Values:\n", df.nunique())
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df.describe(include='all'))

df['Smoothed Screen Time'] = df['Screen Time (hrs/day)'].rolling(window=3, min_periods=1).mean()
print(df[['Screen Time (hrs/day)', 'Smoothed Screen Time']].head())


df_encoded = pd.get_dummies(df, columns=['Gender', 'OS'], drop_first=False)

encoded_columns = [col for col in df_encoded.columns if 'Gender' in col or 'OS' in col]

df_encoded[encoded_columns] = df_encoded[encoded_columns].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

print(df_encoded[encoded_columns].head())




