import pandas as pd

sales = pd.read_csv('data/raw/superstore.csv')

print(sales.head())

sales.to_sql(
    'sales',
    engine,
    if_exists='append',
    index=False
)

print("Data inserted successfully!")