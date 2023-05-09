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

    