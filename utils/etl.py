# this file is used to extract, transform and load data from the database using pandas
import pandas as pd
import numpy as np
import utils.functions as utility
import utils.load_files as lf
import multiprocessing as mp
import csv
import logging
import datetime
import warnings

# Suppress the warning
warnings.filterwarnings('ignore')

#set the path of the project
cur_path = utility.helpers.get_project_path()
#current path in etl.py /Users/williamgao/ETL-Tool

class etl:
    def __init__(self, chunksize, db, config):
        self.chunksize = chunksize
        self.file_names = config['file_names']
        self.file_name_compnaies = config['file_name_compnaies']
        self.file_name_states = config['file_name_states']
        self.output_main_file = config['output_main_file']
        self.output_bad_record = config['output_bad_record']
        self.output_column_names = config['output_column_names']
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db = db
        # TODO: move some of these variables to config file

    def process_frame_us_softball_league(self, df, org_name, org_id):
        # load the companies and states data
        companies = lf.load_files.load_text_file_pandas(self.file_name_compnaies)
        states = lf.load_files.load_text_file_pandas(self.file_name_states)

        #split the name column into first_name and last_name columns and replace the name column with the two new columns
        df = utility.helpers.split_name_in_df(df)

        # add a unique id for each customer becuase there could be customers with same name and dob and same if from the two organizations, 
        # they could even be the same person
        df.insert(0, 'customer_id', [str(org_id)]*len(df) + df['id'].astype(str))

        #transform the date to YYYY-MM-DD format
        df['dob'] = pd.to_datetime(df['date_of_birth'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

        #transform the last_activate to YYYY-MM-DD format
        df['last_active'] = pd.to_datetime(df['last_active'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

        #convert state to abbreviation
        df = pd.merge(df, states, left_on='us_state', right_on='State', how='left')
        df = df.drop(['us_state', 'State'], axis=1)

        #convert company company id to company name
        df = pd.merge(df, companies, left_on='company_id', right_on='id', how='left')
        df = df.drop(['company_id'], axis=1)

        #add source_org column
        df['source_org'] = org_name

        #add created_at, updated_at, deleted_at columns
        df['created_at'] = self.current_time
        df['updated_at'] = self.current_time
        df['deleted_at'] = np.nan

        # df.to_csv('test.csv', index=False)

        #rename columns to match the output column names
        df.rename(columns={'id_x':'original_customer_id', 
                    'joined_league': 'member_since', 
                    'state_code': 'state',
                    'name': 'company_name'
                    }, inplace=True)
        
        df = df[self.output_column_names]
        
        #label records as good or bad
        df['is_suspect'] = df.apply(lambda row: utility.helpers.check_suspect_record(row), axis=1)
        df_main = df[df['is_suspect'] == False][self.output_column_names]
        df_bad = df[df['is_suspect'] == True][self.output_column_names]

        return df_main, df_bad

    def process_frame_unity_golf_club(self, df, org_name, org_id):
        # load the companies and states data
        companies = lf.load_files.load_text_file_pandas(self.file_name_compnaies)

        # add a unique id for each customer becuase there could be customers with same name and dob and same if from the two organizations, 
        # they could even be the same person
        df.insert(0, 'customer_id', [str(org_id)]*len(df) + df['id'].astype(str))

        #transform the date to YYYY-MM-DD format
        df['dob'] = pd.to_datetime(df['dob'], format='%Y/%m/%d').dt.strftime('%Y-%m-%d')

        #transform the last_activate to YYYY-MM-DD format
        df['last_active'] = pd.to_datetime(df['last_active'], format='%Y/%m/%d').dt.strftime('%Y-%m-%d')

        #convert company company id to company name
        df = pd.merge(df, companies, left_on='company_id', right_on='id', how='left')
        df = df.drop(['company_id'], axis=1)

        #add source_org column
        df['source_org'] = org_name

        #add created_at, updated_at, deleted_at columns
        df['created_at'] = self.current_time
        df['updated_at'] = self.current_time
        df['deleted_at'] = np.nan

        # df.to_csv('test.csv', index=False)

        #rename columns to match the output column names
        df.rename(columns={'id_x':'original_customer_id', 
                    'joined_league': 'member_since', 
                    'name': 'company_name'
                    }, inplace=True)
        
        df = df[self.output_column_names]
        
        #label records as good or bad
        df['is_suspect'] = df.apply(lambda row: utility.helpers.check_suspect_record(row), axis=1)
        df_main = df[df['is_suspect'] == False][self.output_column_names]
        df_bad = df[df['is_suspect'] == True][self.output_column_names]

        return df_main, df_bad

    def main_job(self):
        pass