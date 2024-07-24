import pandas as pd

df = pd.read_csv('JEERAKS.csv')

def predict(rank, gender, caste, branch):
    if branch == 'None':
        val = df[df['rank_2024'] >= rank]
        val_x = val[val['gender'] == gender]
        val_y = val_x[val_x['caste'] == caste]
        temp = val_y
    else:
        val = df[df['rank_2024'] >= rank]
        val_x = val[val['gender'] == gender]
        val_y = val_x[val_x['caste'] == caste]
        val_z = val_y[val_y['branch'] == branch]
        temp = val_z
    
    y = temp.sort_values(by='rank_2024', ascending=True)
    z = y.drop_duplicates(subset=["college", "branch"], keep='last')
    return z

def list_of_colleges():
    res = df.college.unique().tolist()
    return res

def branch_list(college):
    college_df = df[df['college'] == college]
    branches = college_df.branch.unique().tolist()
    return branches

def college_branch_data(college, branch):
    college_df = df[df['college'] == college]
    branches = college_df[college_df['branch'] == branch]
    return branches

def fees(college):
    college_df = df[df['college'] == college]
    return college_df.fee.unique().tolist()[0]
