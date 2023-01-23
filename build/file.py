import shutil

def load_string(filepath: str):
    with open(filepath, 'r') as f:
        return f.read()

def save_string(text: str, filepath: str):
    with open(filepath, 'w') as f:
        f.write(text)

def copy(source: str, destination: str):
    shutil.copy(source, destination)
