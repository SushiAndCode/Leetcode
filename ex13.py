import pandas as pd

# Creating the Employee DataFrame
employee_data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
    "salary": [70000, 90000, 80000, 60000, 90000],
    "departmentId": [1, 1, 2, 2, 1]
}
employee_df = pd.DataFrame(employee_data)

# Creating the Department DataFrame
department_data = {
    "id": [1, 2],
    "name": ["IT", "Sales"]
}
department_df = pd.DataFrame(department_data)

indexes = employee_df.groupby(by=["departmentId"])

maxes = employee_df.iloc(set(indexes["id"].values))