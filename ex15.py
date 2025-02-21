import pandas as pd

data = pd.DataFrame({
    "id": [1, 2, 3],
    "email": ["john@example.com", "bob@example.com", "john@example.com"]
})

data = data.groupby(by = "email").apply(lambda x: x[x["id"] == x["id"].min()]).reset_index(drop=True)

print(data)

