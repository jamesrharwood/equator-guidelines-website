from .read import file_to_str 
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.how_to_use, guideline.destination_paths.how_to_use)
    return file_to_str('_how_to_use.qmd')