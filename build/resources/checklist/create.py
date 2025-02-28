import os 
from pathlib import Path

from build.file import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
PATH = str(Path(dir_path, 'template.md'))


def create(guideline):
    copy(PATH, guideline.destination_paths.checklist)
