#unit test for functions using pytest library
import os, sys
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if cur_path not in sys.path:
    sys.path.append(cur_path)
import utils.load_files as lf
import utils.database as database
#initialize the database
db = database.Database()

# unit test for executing query in db 
def test_exe_read_query():
    assert db.connect_db_and_run_query('query/test.sql') > 0

# unit test for executing query in db 
def test_exe_create_query():
    assert db.connect_db_and_run_query('query/model_membership.sql') > 0
