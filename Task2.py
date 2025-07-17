import pandas as pd

df = pd.read_csv('phone_usage_india.csv')

print(df)

print("\nMean Values:")
print(df.mean(numeric_only=True))

print("\nMedian Values:")
print(df.median(numeric_only=True))

print("\nMode Values:")
print(df.mode().iloc[0])


print("Variation:")

range_data = df.max(numeric_only=True) - df.min(numeric_only=True)
print("\nRange:")
print(range_data)

print("\nVariance:")
print(df.var(numeric_only=True))

print("\nStandard Deviation:")
print(df.std(numeric_only=True))


crosstab = pd.crosstab(df['Location'], df['Phone Brand'])
print("Cross-tabulation: Location vs Phone Brand")
print(crosstab, "\n")

phone_brand_freq = df['Phone Brand'].value_counts()
print("Phone Brand Frequency Distribution")
print(phone_brand_freq, "\n")

