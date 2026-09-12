import pandas as pd

df = pd.read_csv("data/raw/HI-Small_Trans.csv")

df = df.rename(
    columns={
        "Account": "From Account",
        "Account.1": "To Account",
    }
)

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    format="%Y/%m/%d %H:%M"
)

train = df[
    (df["Timestamp"] >= "2022-09-01")
    & (df["Timestamp"] < "2022-09-07")
]

val = df[
    (df["Timestamp"] >= "2022-09-07")
    & (df["Timestamp"] < "2022-09-09")
]

test = df[
    (df["Timestamp"] >= "2022-09-09")
    & (df["Timestamp"] < "2022-09-11")
]

print("Train:", len(train), "transactions |", train["Is Laundering"].sum(), "class-1")
print("Validation:", len(val), "transactions |", val["Is Laundering"].sum(), "class-1")
print("Test:", len(test), "transactions |", test["Is Laundering"].sum(), "class-1")

print("Train dates:", train["Timestamp"].min(), "to", train["Timestamp"].max())
print("Validation dates:", val["Timestamp"].min(), "to", val["Timestamp"].max())
print("Test dates:", test["Timestamp"].min(), "to", test["Timestamp"].max())

df["hour_of_day"] = df["Timestamp"].dt.hour
print(df[["Timestamp", "hour_of_day"]].head())

df["same_currency"] = (
    df["Payment Currency"] == df["Receiving Currency"]
).astype(int)
print(
    df[
        ["Payment Currency", "Receiving Currency", "same_currency"]
    ].head()
)

print("Exact duplicate rows kept:", df.duplicated().sum())