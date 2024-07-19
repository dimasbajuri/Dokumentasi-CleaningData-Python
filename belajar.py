import pandas as pd

data_csv = pd.read_csv("bad_data.csv")

data_csv.loc[4, 'Age'] = 30

# data_csv["Age"] = data_csv["Age"].ffill()

# data_csv["Score"] = data_csv["Score"].fillna(data_csv["Score"].mean())

# data_csv["Age"] = pd.to_numeric(data_csv["Age"])

# data_csv.loc[6, "Name"] = "Jonathan Doe"
# data_csv.loc[6, "Email"] = "jonathandoe@example.com"

# data_csv.loc[3, "Date_of_Birth"] = "1999-12-31"
data_csv["Age"] = data_csv["Age"].ffill()
data_csv["Score"] = data_csv["Score"].bfill()
print(data_csv)