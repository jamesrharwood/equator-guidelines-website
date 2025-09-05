import os 
from pathlib import Path

from build.file import load_string, save_string

dir_path = os.path.dirname(os.path.realpath(__file__))
PATH = str(Path(dir_path, 'template.md'))
PLACEHOLDER = '{TABLE}'

def create(guideline):
    from .guideline import Guideline

    guideline = Guideline.create(guideline.id)
    string = load_string(PATH)
    assert PLACEHOLDER in string
    md = guideline.get_table_markdown()
    string = string.replace(PLACEHOLDER, md)
    save_string(string, guideline.destination_paths.checklist)
