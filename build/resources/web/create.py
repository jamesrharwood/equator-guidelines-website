import os
import re
import shutil

from .partials import PARTIALS
from build.file import save_string

def create(guideline):
    qmd = create_qmd(guideline)
    save_string(qmd, guideline.destination_paths.index)

def create_qmd(guideline):
    strings = get_partial_strings(guideline)
    qmd = '\n\n'.join(strings)
    return qmd
    
def get_partial_strings(guideline):
    for partial in get_partials(guideline):
        yield(partial.create_web(guideline))

def get_partials(guideline):
    for partial in PARTIALS:
        if partial.required_by_guideline(guideline):
            yield partial