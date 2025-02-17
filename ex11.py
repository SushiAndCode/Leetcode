import pandas as pd

employees = pd.DataFrame({
    "id": [1, 2,3,4,5,6,7,8],
    "num": [100,10,100,22,40,40,50,200],
    "man_id":[7,8,None,None,None,None,None,None]
})


manag = employees[employees["man_id"].isnull()]

emp = employees[employees["man_id"].notnull()]

merged = emp.merge(manag, left_on="man_id", right_on="id", suffixes=('_emp', '_man'))

paidMore = merged[merged["num_emp"] > merged["num_man"]]

print(paidMore)