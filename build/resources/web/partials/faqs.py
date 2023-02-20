from .read import file_to_str
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.faqs, guideline.destination_paths.faqs)
    return file_to_str('_faqs.qmd')
