import re

num_rx = re.compile(r'\d')
underscore_rx = re.compile('_')

def validate_id(id: str):
    assert id == id.lower(), 'IDs must be lower case'
    assert ' ' not in id, 'IDs must not contain spaces'
    assert not num_rx.search(id)
    assert not underscore_rx.search(id)