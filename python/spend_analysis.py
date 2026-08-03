import pandas as pd

df = pd.read_csv('../data/spend_analysis_dataset.csv')
summary = df.groupby('Category')['TotalCost'].sum().reset_index()
summary.to_csv('../outputs/category_spend.csv', index=False)
print(summary)
