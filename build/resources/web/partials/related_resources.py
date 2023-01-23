from .read import file_to_str 
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.related_resources, guideline.destination_paths.related_resources)
    return file_to_str('_related_resources.qmd')