from .read import file_to_str

def create_web(guideline):
    string = "## Training and Support\n\n"
    string += file_to_str('../../partials/training/default.md')
    return string