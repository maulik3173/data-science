import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('phone_usage_india.csv')
print(df)

sns.set(style="whitegrid")

num_cols = df.select_dtypes(include=['float64', 'int64']).columns

plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Age'], color='salmon')
plt.title("Box Plot of Age")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
sns.stripplot(x="Primary Use", y="Age", data=df, jitter=True, palette="coolwarm")
plt.title("Dot Plot of Screen Time by Primary Use")
plt.xlabel("Primary Use")
plt.ylabel("Age")
plt.tight_layout()
plt.grid(True)
plt.show()

# for col in num_cols:
#     plt.figure(figsize=(8, 4))
#     sns.histplot(df[col], kde=False, bins=30, color='salmon')
#     plt.title(f"Histogram of {col}")
#     plt.xlabel(col)
#     plt.ylabel("Frequency")
#     plt.tight_layout()
#     plt.show()


# for col in num_cols:
#     Q1 = df[col].quantile(0.25)
#     Q3 = df[col].quantile(0.75)
#     IQR = Q3 - Q1
#     outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
#     print(f'Outliers in {col}: \n',outliers)
