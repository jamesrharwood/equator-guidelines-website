from build.file import copy
from ..utils import copy_file_adding_glossary

def create_web(guideline):
    copy_file_adding_glossary(guideline, 'why_use', dicts=[guideline.glossary_default_dict, guideline.glossary_dict])
    return ''
