import pandas as pd

df = pd.read_csv('phone_usage_india.csv')

print(df)

print("Missing values in each column:")
print(df.isnull().sum())

df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Phone Brand'] = df['Phone Brand'].fillna(df['Phone Brand'].mode()[0])
df['Screen Time (hrs/day)'] = df['Screen Time (hrs/day)'].fillna(df['Screen Time (hrs/day)'].mean())
df['Number of Apps Installed'] = df['Number of Apps Installed'].fillna(df['Number of Apps Installed'].mean())

print("Missing values after handling:")
print(df.isnull().sum())

print("\nDuplicate rows in the DataSet:")
print(df.duplicated().sum())

df.to_csv('cleaned_phone_usage_india.csv', index=False)