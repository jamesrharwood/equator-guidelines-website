import re

from typing import Callable
from markdown import Markdown

def add_glossary_to_string_using_spans(string, glossary_dict):
    return add_glossary_to_string(string, glossary_dict, wrapper_fn=wrap_string_with_span)

def add_glossary_to_string(string: str, glossary_dict: dict, wrapper_fn: Callable) -> str:
    if not glossary_dict:
        return string
    matches = find_matches(string, glossary_dict)
    matches = filter_matches(matches)
    matches.reverse()
    for match in matches:
        id_ = get_match_id(match)
        start = match.start()
        end = match.end()
        tagged_string = wrapper_fn(string[start:end], id_)
        string = string[:start] + tagged_string + string[end:]
    return string

def filter_matches(matches):
    matches = [match for match in matches if match_should_be_wrapped(match)]
    matches_to_return = []
    match_ids = []
    for match in matches:
        id_ = get_match_id(match)
        if id_ not in match_ids:
            matches_to_return.append(match)
            match_ids.append(id_)
    return matches_to_return

def find_matches(string, glossary_dict):
    pattern = create_regex(glossary_dict)
    matches = list(pattern.finditer(string))
    matches.sort(key=lambda x: x.start())
    return matches

def create_regex(glossary_dict):
    pattern = create_combined_pattern(glossary_dict)
    pattern = re.compile(pattern, flags=re.IGNORECASE)
    return pattern 

def create_combined_pattern(glossary_dict: dict):
    patterns = [create_pattern(dict_entry) for dict_entry in glossary_dict.values()]
    pattern = "|".join(patterns)
    return pattern

def create_pattern(dict_entry):
    id_ = dict_entry['id']
    group_id = glossary_id(id_)
    pattern = dict_entry['pattern']
    return rf'\b(?P<{group_id}>{pattern})\b'

def wrap_string_with_span(string: str, id_: str):
    return SPAN.format(id_=id_, string=string)

def get_match_id(match):
    groupdict = {k:v for k,v in match.groupdict().items() if v}
    id = list(groupdict.keys())[0]
    return id

def glossary_id(id_: int|str):
    return f'glossaryItem{id_}'

def transform_dict(dct):
    new_dict = {}
    for idx, k in enumerate(dct.keys()):
        v = dct[k]
        if type(v) == str:
            new_dict.update({k: {
                'pattern': k,
                'text': v,
                'title': k.capitalize(),
                'index': idx,
                'id': idx
            }})
        else:
            v.update({'index': idx})
            new_dict.update({k: v})
    md = Markdown()
    for k, v in new_dict.items():
        v.update({'text': md.convert(v['text'])})
    return new_dict

SPAN = """\
<span class="defined" data-bs-toggle="offcanvas" href="#{id_}" aria-controls="offcanvasExample" role="button">{string}</span>"""

def match_should_be_wrapped(match):
    if is_a_link(match):
        return False
    if is_an_aside(match):
        return False
    if is_a_title(match):
        return False
    if is_in_metadata(match):
        return False
    return True

LINK_START = re.compile(r'\]\([^\)]*$')
ASIDE_START = re.compile(r'\[[^\[]*$')
HEADING = re.compile(r'^#+')

def is_a_title(match):
    if match.start() == 0:
        return False
    string = match.string[:match.start()]
    string = string.splitlines()[-1]
    return HEADING.search(string)

def is_in_metadata(match):
    metadata_splitter = '---'
    if metadata_splitter in match.string[:match.start()]:
        if metadata_splitter in match.string[match.end():]:
            return True

def is_a_link(match):
    return LINK_START.search(match.string[:match.start()])

def is_an_aside(match):
    return ASIDE_START.search(match.string[:match.start()])

