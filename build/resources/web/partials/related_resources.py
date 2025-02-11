from ..utils import copy_file_adding_glossary
from .read import file_to_str

def create_web(guideline):
    copy_file_adding_glossary(guideline, 'related_resources')
    return file_to_str('_related_resources.qmd')