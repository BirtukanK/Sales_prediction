import pandas as pd

store_data = pd.read_csv("../data/store.csv")
train_data = pd.read_csv("../data/train.csv")

merged_data = store_data.merge(train_data, on=["Store"])
merged_data.head()
joined_data = pd.to_csv()