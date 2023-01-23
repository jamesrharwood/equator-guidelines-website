from .read import file_to_str
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.use_for, guideline.destination_paths.use_for)
    return file_to_str('_use_for.qmd')
    