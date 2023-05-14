import logging
import utils.etl
import utils.database as database
import utils.functions as utility
import utils.load_files as lf

#set the path of the project
cur_path = utility.helpers.get_project_path()

def main():
    
    #load config parameters
    try:
        config = lf.load_files.load_config()  
    except Exception as err:
        logging.error(f'Error loading config file: {err}')
        return 
    
    #initialize the database
    db = database.Database()
    # execute query to create data model 
    db.connect_db_and_run_query('query/model_companies.sql', read=False)
    db.connect_db_and_run_query('query/model_membership.sql', read=False)
    
    #initiate etl object 
    jobs = utils.etl.etl(config['chunksize'], db, config)
    # run etl with chunksize from config file
    jobs.main_job()


if __name__ == "__main__":
    main()
# this is a test