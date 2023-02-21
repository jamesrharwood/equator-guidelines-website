from .read import file_to_str
from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.how_to_cite, guideline.destination_paths.how_to_cite)
    return '## How to cite\n\n{{< include partials/how_to_cite.md >}}'

