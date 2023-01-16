from .read import file_to_str

def create_web(guideline):
    string = file_to_str('_download_resources.qmd')
    return string.replace('ID', guideline.id)
