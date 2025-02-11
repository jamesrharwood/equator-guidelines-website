from ..utils import copy_file_adding_glossary
from .read import file_to_str

def create_web(guideline):
    copy_file_adding_glossary(guideline, 'not_use_for')
    return file_to_str('_not_use_for.qmd')