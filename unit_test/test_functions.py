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
