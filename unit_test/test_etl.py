#unit test for functions using pytest library
import os, sys, logging
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if cur_path not in sys.path:
    sys.path.append(cur_path)
import utils.load_files as lf
import utils.etl as etl
import utils.database as database

# unit test function process_frame_us_softball_league in etl.py
def test_process_frame_us_softball_league():
    #load config parameters
    try:
        config = lf.load_files.load_config()  
    except Exception as err:
        logging.error(f'Error loading config file: {err}')
        return 
    #initialize the database
    db = database.Database()
    etl_obj = etl.etl(2, db, config)
    reader = lf.load_files.load_text_file_pandas_chunk('us_softball_league.tsv', chunksize=2)
    for df in reader:
        df_main, df_bad = etl_obj.process_frame_us_softball_league(df, 'us_softball_league.tsv', '1000000')
        assert df_main.columns.to_list() == ['customer_id', 'first_name', 'last_name', 'original_customer_id', 'dob','company_name','last_active','score','member_since','state', 'source_org', 'created_at','updated_at', 'deleted_at']