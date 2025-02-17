import pandas as pd


logs = pd.DataFrame({
    "id": [1, 2,3,4,5,6],
    "num": [100, 100,100,22,40,40]
})

df = pd.DataFrame()
logs["count"] = logs.groupby(logs["num"].ne(logs["num"].shift()).cumsum()).cumcount()+1
df["ConsecutiveNums"] = logs["num"][logs["count"] == 3].reset_index(drop = True)

print(df)