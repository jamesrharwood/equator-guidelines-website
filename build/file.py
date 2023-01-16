def load_string(filepath: str):
    with open(filepath, 'r') as f:
        return f.read()

def save_string(text: str, filepath: str):
    with open(filepath, 'w') as f:
        f.write(text)