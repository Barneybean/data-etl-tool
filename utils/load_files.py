import yaml
import logging
import pandas as pd
import utils.functions as utility

cur_path = utility.helpers.get_project_path()

class load_files:
    
    def load_config():
        # read config yaml, stop the process if error
        with open("config.yml", "r") as stream:
            try:
                config = yaml.safe_load(stream)
                # print('current config: ', config)
                logging.info('current config: ', config)
                return config
            except yaml.YAMLError as exc:
                # print(exc)
                logging.error(exc)
                return 
    
    #load query from sql file and return as a string
    def load_query_text(query_file_path):
        with open(query_file_path, 'r') as fd:
            sq_file = fd.read()
            fd.close()
        return sq_file
    
    def load_text_file_pandas(file_name):
        if '.tsv' in file_name:
            df = pd.read_csv(cur_path + '/input/'+ file_name, sep='\t')
        
        if '.csv' in file_name:
            df = pd.read_csv(cur_path + '/input/'+ file_name)
        return df
    
    def load_text_file_pandas_chunk(file_name, chunksize):
        if '.tsv' in file_name:
            df = pd.read_csv(cur_path + '/input/'+ file_name, sep='\t', chunksize=chunksize)
        
        if '.csv' in file_name:
            df = pd.read_csv(cur_path + '/input/'+ file_name, chunksize=chunksize)
        return df