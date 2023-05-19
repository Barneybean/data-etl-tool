#boiler plate of postgres connections and cursor
import utils.load_files as lf
from sqlalchemy import create_engine
import psycopg2
import os, logging

#database connection and executions
class Database:
    def __init__(self):
        #get environment variables
        self.db_user = os.environ.get('POSTGRES_USER')
        self.db_password = os.environ.get('POSTGRES_PASSWORD')
        self.db_host = os.environ.get('POSTGRES_HOST')
        self.db_port = os.environ.get('POSTGRES_PORT')
        self.db_name = os.environ.get('POSTGRES_DATABASE')
        self.conn_string = 'postgresql://'+self.db_user+':'+self.db_password+'@'+self.db_host+':'+self.db_port+'/'+self.db_name

    def connect(self):
        db = create_engine(self.conn_string)
        conn = db.connect()
        return conn

    def ingest_df_to_db(self, df, table_name):
        conn = self.connect()
        # load dataframe to database

        try:
            df.to_sql(table_name, con=conn, if_exists='append', index=False, schema='public')
        except Exception as err:
            print("!"*30)
            print('database conn error! ')
            print(err)
            print("!"*30)
            logging.info("!"*30)
            logging.info('database conn error! ')
            logging.error(err)
            logging.info("!"*30)
            
        conn.close()
    
    def connect_db_and_run_query(self, file_path, read=True):
        #execute query scripts from query folder
        conn = psycopg2.connect(self.conn_string)
        conn.autocommit = True
        cursor = conn.cursor()

        query = lf.load_files.load_query_text(file_path)
        try:
            cursor.execute(query)
            if read:
                results = cursor.fetchall()
                for i in results[:3]:
                    logging.info(i)
        except Exception as err:
            print("!"*30)
            print('database conn error! ')
            print(err)
            print("!"*30)
            logging.info("!"*30)
            logging.info('database conn error! ')
            logging.error(err)
            logging.info("!"*30)
        
        conn.close()
        return 1
