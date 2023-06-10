from .read import file_to_str 
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.why_use, guideline.destination_paths.why_use)
    return ''
    # return file_to_str('_why_use.qmd')