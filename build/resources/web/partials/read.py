import os
from pathlib import Path

dirpath = os.path.abspath(__file__)
dirpath = Path(dirpath).parent.absolute()

def file_to_str(filename):
    path = os.path.join(dirpath, filename)
    return path_to_str(path)

def path_to_str(path):
    with open(path, 'r') as file_:
        return file_.read()

def replace_ID(string, guideline):
    string = string.replace('ID', guideline.id)
    return string
