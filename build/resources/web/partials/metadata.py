from .read import file_to_str
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.metadata, guideline.destination_paths.metadata)
    return ''