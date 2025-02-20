from ..utils import copy_file_adding_glossary
from .read import file_to_str

def create_web(guideline):
    copy_file_adding_glossary(guideline, 'related_resources', dicts=[guideline.glossary_default_dict, guideline.glossary_dict])
    return file_to_str('_related_resources.qmd')