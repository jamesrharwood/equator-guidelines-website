import shutil
import yaml


def load_string(filepath: str):
    with open(filepath, 'r') as f:
        return f.read()

def save_string(text: str, filepath: str):
    with open(filepath, 'w') as f:
        f.write(text)

def copy(source: str, destination: str):
    shutil.copy(source, destination)

def get_yml(path):
    with open(path, 'r') as file_:
        yml = yaml.safe_load(file_)
    return yml

def save_yml(path, yml):
    with open(path, 'w') as file_:
        yaml.safe_dump(yml, file_)