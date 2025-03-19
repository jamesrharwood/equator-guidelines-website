from build.file import load_string, save_string
from build.guideline.glossary import add_glossary_to_string_using_spans

def copy_file_adding_glossary(guideline, attr, dicts=None):
    dicts = dicts if dicts else [guideline.glossary_dict]
    combined_dict = combine_dicts(dicts)
    string = load_string(getattr(guideline.repo_paths, attr))
    string = add_glossary_to_string_using_spans(string, combined_dict)
    save_string(string, getattr(guideline.destination_paths, attr))

def combine_dicts(dicts):
    combined_dict = dicts[0]
    for dict in dicts[1:]:
        for key, value in dict.items():
            combined_dict[key].update({'text': value['text']})
    return combined_dict
