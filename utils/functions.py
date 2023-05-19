# this file is to store all the helper functions that can be used across the project
import os, sys
import csv

class helpers:

    def __init__(self):
        pass

    # this function is to get the project path
    def get_project_path():
        cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if cur_path not in sys.path:
            sys.path.append(cur_path)
        # this should return current path in etl.py /Users/williamgao/ETL-Tool
        return cur_path

    #create new csv files if not exist
    def create_csv_files(path, columns):
        # Create the output file if it doesn't exist
        if not os.path.isfile(path):
            with open(path, "w", newline="\n") as output_file:
                # Create CSV reader and writer objects
                csv_writer = csv.writer(output_file)
                # Write the header row to the output file with the new column name 
                csv_writer.writerow(columns)

    def split_name_in_df(df):
        #split the name column into first_name and last_name columns and replace the name column with the two new columns
        if len(df)>0:
            df[['first_name', 'last_name']] = df['name'].str.split(' ', expand=True)
            # Drop the original name column
            df.drop('name', axis=1, inplace=True)

            # Reorder the columns so that first_name and last_name come first
            df = df[['first_name', 'last_name'] + list(df.columns[:-2])]
        else:
            pass
        return df 

    def check_suspect_record(row):
        #check if the record is a suspect record
        result = False
        # check if the dob > last_active
        if str(row['dob']) > str(row['last_active']):
            result = True
        
        # check if the member_since > last_active
        if str(row['member_since']) > str(row['last_active']):
            result = True
        
        #check if the dob > member_since
        if str(row['dob']) > str(row['member_since']):
            result = True

        # if first name or last name is null, then it is a suspect record
        if row['first_name'] == None or row['last_name'] == None:
            result = True
            
        return result
