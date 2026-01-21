import datetime

import pandas as pd

csv_dir = "data/sales_orders_dataset.csv"

json_dir = "data/sales_orders_dataset.json"
# used to load, clean, transform and analyze structured data.


# ages = pd.Series([10,20,30])
# print(ages)

d_csv = pd.read_csv(csv_dir)
# print(d_csv.info())

d_json = pd.read_json(json_dir)

# print(d_json.isnull().sum())
# print(d_json.info())
# d_json['order_date'] = d_json['order_date'].astype('datetime64[ns]')
# print(d_json.info())

# print(d_json[d_json["unit_price"]>400])

# print(d_json[["customer_id","total_amount"]])

# print(d_json["customer_id"].unique())

# print(d_json.sort_values(by=['total_amount'], ascending=False))

# print(d_json.groupby('customer_id')['total_amount'].sum()) # --> select cust_id,sum(total_amount) from dataset group by cust_id

# print(pd.merge(d_json , d_csv, on='customer_id', how='inner').info())

# select * from a1 join a2 on a1.id=a2.id;


print(d_csv.shape)
print(len(d_csv))
print(d_csv.iloc[9])
