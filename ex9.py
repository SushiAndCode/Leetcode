import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee.sort_values(by = 'salary', ascending = False, inplace = True, ignore_index = True)
    employee.rename(columns = {'salary':'SecondHighestSalary'},inplace = True)
    employee.drop_duplicates(subset=["SecondHighestSalary"],inplace = True,ignore_index=True)
    if len(employee["SecondHighestSalary"])>1:
        return employee.loc[[1],['SecondHighestSalary']]
    else:
        return pd.DataFrame([None],columns = ['SecondHighestSalary'])
    
df = pd.DataFrame({
    "id": [1, 2,3],
    "salary": [100, 100,50]
})

second_highest_salary(df)