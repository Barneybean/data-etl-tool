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
    except Exception as e:
        return 

if __name__ == "__main__":
    main()