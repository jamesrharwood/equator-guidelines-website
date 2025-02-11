from .read import file_to_str, replace_ID
from build.guideline.glossary import add_glossary_to_string_using_spans
def create_web(guideline):
    string = file_to_str('_how_to_use.qmd')
    string = replace_ID(string, guideline)
    string = add_glossary_to_string_using_spans(string, guideline.glossary_default_dict)
    return string

