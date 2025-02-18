import pandas as pd

employee = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": ["Joe", "Jim", "Henry", "Sam", "Max", "Hek", "Norm", "Kate", "Lyod", "Frank"],
    "salary": [70000, 90000, 80000, 60000, 90000, 75000, 60000, 90000, 89000, 89000],
    "departmentId": [1, 1, 2, 2, 1, 1, 2, 1, 1, 1]
})

department = pd.DataFrame({
    "id": [1,2],
    "name": ["IT","Business"]
})

employee["rank"] = employee.groupby(by=["departmentId"])["salary"].rank(method="dense", ascending=False)

employee = employee.sort_values(by=["departmentId","rank"],ascending=False).reset_index(drop=True)

employee = employee.groupby(by="departmentId").apply(lambda x: x[x["rank"] > (x["rank"].max() - 3)]).reset_index(drop=True)

ans = employee.merge(department, left_on = "departmentId", right_on = "id")

ans = ans[["name_x","name_y","salary"]].rename(columns = {"name_x": "Employee", "salary": "Salary", "name_y": "Department"})

print(ans)

