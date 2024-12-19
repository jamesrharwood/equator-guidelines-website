def validate_id(id: str):
    assert id == id.lower(), 'IDs must be lower case'
    assert ' ' not in id, 'IDs must not contain spaces'