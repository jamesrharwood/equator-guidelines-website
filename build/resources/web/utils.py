from build.file import load_string, save_string
from build.guideline.glossary import add_glossary_to_string_using_spans

def copy_file_adding_glossary(guideline, attr, dicts=None):
    dicts_to_add = dicts if dicts else [guideline.glossary_dict]
    string = load_string(getattr(guideline.repo_paths, attr))
    for dict in dicts_to_add:
        string = add_glossary_to_string_using_spans(string, dict)
    save_string(string, getattr(guideline.destination_paths, attr))
