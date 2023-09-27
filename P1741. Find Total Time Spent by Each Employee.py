import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    time_spent_office = employees['out_time'] - employees['in_time']
    
    employees['total_time'] = time_spent_office
    
    
    grouped_employees = employees.groupby(['event_day', 'emp_id'], as_index=False)
    
     
    total_employees= grouped_employees.agg(sum)

    
    renamed_employee_df = total_employees.rename(columns={'event_day': 'day'})
    
    
    new_employee_df = renamed_employee_df.drop(columns=['out_time', 'in_time'])
    
    return new_employee_df