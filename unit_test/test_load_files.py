#unit test for functions using pytest library
import os, sys
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if cur_path not in sys.path:
    sys.path.append(cur_path)

import utils.load_files as lf

#unit test for load config
def test_load_config():
    assert len(lf.load_files.load_config()) > 0

# unit test for loading sql
def test_load_query():
    assert len(lf.load_files.load_query_text('query/test.sql')) > 0
