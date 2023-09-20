import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    result_df = users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com')]
    return result_df