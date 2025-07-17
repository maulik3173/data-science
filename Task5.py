import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('phone_usage_india.csv')
print(df)

age_bins = [10, 20, 30, 40, 50, 60, 70]
age_labels = ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69']
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

metrics_by_age = df.groupby('Age Group')[
    ['Screen Time (hrs/day)', 'Data Usage (GB/month)',
     'Social Media Time (hrs/day)', 'Gaming Time (hrs/day)', 'Streaming Time (hrs/day)']
].mean()


plt.figure(figsize=(12, 6))
for col in metrics_by_age.columns:
    sns.lineplot(data=metrics_by_age[col], label=col)
    
plt.title("Usage Trends Across Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Average Usage")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
