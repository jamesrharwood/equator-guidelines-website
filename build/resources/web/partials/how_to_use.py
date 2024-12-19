from .read import file_to_str, replace_ID
from build.file import copy

def create_web(guideline):
    string = file_to_str('_how_to_use.qmd')
    string = replace_ID(string, guideline)
    return string

