from .read import file_to_str
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.not_use_for, guideline.destination_paths.not_use_for)
    return file_to_str('_not_use_for.qmd')