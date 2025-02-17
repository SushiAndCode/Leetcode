import pandas as pd

employees = pd.DataFrame({
    "id": [1, 2,3,4,5,6,7,8],
    "num": [100,10,100,22,40,40,50,200],
    "man_id":[7,8,None,None,None,None,None,None]
})

counter = employees.value_counts(subset="num")

print(counter.loc[counter >1].index)
