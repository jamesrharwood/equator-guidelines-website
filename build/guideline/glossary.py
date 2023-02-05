import re

from typing import Callable

def add_glossary_to_string(string: str, glossary_dict: dict, wrapper_fn: Callable) -> str:
    if not glossary_dict:
        return string
    matches = find_matches(string, glossary_dict)
    matches.reverse()
    for match in matches:
        start = match.start()
        end = match.end()
        id_ = get_match_id(match)
        tagged_string = wrapper_fn(string[start:end], id_)
        string = string[:start] + tagged_string + string[end:]
    return string

def find_matches(string, glossary_dict):
    pattern = create_regex(glossary_dict)
    matches = list(pattern.finditer(string))
    return matches

def create_regex(glossary_dict):
    pattern = create_combined_pattern(glossary_dict)
    pattern = re.compile(pattern, flags=re.IGNORECASE)
    return pattern 

def create_combined_pattern(glossary_dict: dict):
    patterns = [create_pattern(key, index) for index, key in enumerate(glossary_dict.keys())]
    pattern = "|".join(patterns)
    return pattern

def create_pattern(string: str, index:int):
    group_id = id_from_index(index)
    return rf'\b(?P<{group_id}>{string})\b'

def wrap_string_with_span(string: str, id_: str):
    return SPAN.format(id_=id_, string=string)

def get_match_id(match):
    groupdict = {k:v for k,v in match.groupdict().items() if v}
    id = list(groupdict.keys())[0]
    return id

def id_from_index(index: int):
    return f'glossaryItem{index}'

SPAN = """\
<span class="defined" data-bs-toggle="offcanvas" href="#{id_}" aria-controls="offcanvasExample" role="button">{string}</span>"""