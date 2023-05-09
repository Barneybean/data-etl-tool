#unit test for functions using pytest library
import os, sys
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if cur_path not in sys.path:
    sys.path.append(cur_path)

import utils.functions as utility
import pandas as pd

#unit test for get_project_path function
def test_cur_path():
    assert utility.helpers.get_project_path() == '/Users/williamgao/data-etl-tool'

#unit test for create_csv_files function, column = ['customer_id', 'first_name', 'last_name', 'original_customer_id', 'dob','company_name','last_active','score','member_since','state', 'source_org', 'created_at','updated_at', 'deleted_at']
def test_create_csv_files():
    #create a test csv file
    utility.helpers.create_csv_files('test.csv', ['customer_id', 'first_name', 'last_name', 'original_customer_id', 'dob','company_name','last_active','score','member_since','state', 'source_org', 'created_at','updated_at', 'deleted_at'])
    #read the test csv file
    df = pd.read_csv('test.csv')
    #check if the test csv file has the same column as the original csv file
    assert df.columns.tolist() == ['customer_id', 'first_name', 'last_name', 'original_customer_id', 'dob','company_name','last_active','score','member_since','state', 'source_org', 'created_at','updated_at', 'deleted_at']
    #delete the test csv file
    os.remove('test.csv')


#unit test for split_name_in_df function
def test_split_name_in_df():
    #create dummy dataframes with name column
    df = pd.DataFrame({'name': ['Kevin Gao', 'William Gao', 'John Gao']})
    df = utility.helpers.split_name_in_df(df)
    assert df['first_name'].tolist() == ['Kevin', 'William', 'John']
    assert df['last_name'].tolist() == ['Gao', 'Gao', 'Gao']

# test to see if the check_suspect_record function works
def test_find_suspective_row():
    #create dummy dataframes with dob, member_since, last_active columns
    df = pd.DataFrame({'dob': ['2020-01-01', '2001-01-01', '2000-01-01'], 
                       'member_since': ['2019-01-01', '2015-01-01', '2020-01-01'], 
                       'last_active': ['2021-01-01', '2020-01-01', '2018-01-01'],
                       'first_name': ['Kevin', 'William', 'John'],
                       'last_name': ['Gao', 'Gao', 'Gao']
                    })
    
    df['is_suspect'] = df.apply(lambda row: utility.helpers.check_suspect_record(row), axis=1)
    assert df['is_suspect'].tolist() == [True, False, True]
