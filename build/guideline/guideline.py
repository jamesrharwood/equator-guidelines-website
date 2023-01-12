import os

from dataclasses import dataclass

import yaml

from .item import Item
from .paths import RepoPaths, DestinationPaths
from ..resources import create_resources

@dataclass
class Guideline:
    repo_paths: RepoPaths
    dest_paths: DestinationPaths
    config: dict
    has_translations: bool
    has_not_use_for: bool
    has_related_resources: bool

    def create_resources(self):
        self.create_folder()
        create_resources(self)
    
    def create_folder(self):
        if not os.path.exists(self.dest_paths.dir):
            os.makedirs(self.dest_paths.dir)
    

def create(dirname:str):
    repo_paths = RepoPaths(dirname)
    config = load_yaml(repo_paths.config)

    return Guideline(
        repo_paths=repo_paths,
        dest_paths=DestinationPaths(dirname),
        config=config,
        has_translations=has_translations(config),
        has_not_use_for=has_text(repo_paths.not_use_for),
        has_related_resources=has_text(repo_paths.related_resources)
    )

def has_translations(config: dict) -> bool:
    return bool(config['translations'])

def load_yaml(filepath):
    with open(filepath, 'r') as file_:
        return yaml.safe_load(file_)

def has_text(filepath):
    return os.path.getsize(filepath)!=0