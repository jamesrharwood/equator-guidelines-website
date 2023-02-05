import os

from dataclasses import dataclass, field

import yaml

from .item import Item
from build.paths import RepoPaths, DestinationPaths, RelativeDestinationPaths
from build.resources import create_resources

# This could be better as a normal class, not dataclass

@dataclass
class Guideline:
    dirname: str
    config: dict
    resource_definitions: dict
    glossary_dict: dict
    repo_paths: RepoPaths = field(init=False)
    destination_paths: DestinationPaths = field(init=False)
    has_translations: bool = field(init=False)
    has_not_use_for: bool = field(init=False)
    has_related_resources: bool = field(init=False)
    id: str = field(init=False)
    doi: str = field(init=False)
    translations: list[dict] = field(init=False)

    def create_resources(self):
        self.create_folder()
        create_resources(self)
    
    def create_folder(self):
        if not os.path.exists(self.destination_paths.dir): # type: ignore
            os.makedirs(self.destination_paths.dir) # type: ignore
            os.makedirs(self.destination_paths.partials_dir)
    
    def __post_init__(self):
        self.repo_paths = RepoPaths(self.dirname)
        self.destination_paths = DestinationPaths(self.dirname)
        self.relative_destination_paths = RelativeDestinationPaths('')
        self.doi = self.config['doi']
        self.translations = self.config.get('translations', [])
        self.id = self.config['id']
        self.has_translations = has_translations(self.config)
        self.has_not_use_for = has_text(self.repo_paths.not_use_for)
        self.has_related_resources=has_text(self.repo_paths.related_resources)
        self.items = list(self.load_items())
    
    def load_items(self):
        item_dir = self.repo_paths.items_dir
        for filename in os.listdir(item_dir):
            path = os.path.join(item_dir, filename)
            yield Item.from_filepath(path)

    @classmethod
    def create(cls, dirname: str):
        paths = RepoPaths(dirname)
        config = load_yaml(paths.config)
        resource_definitions = load_yaml(paths.resource_definitions)
        glossary_dict = load_yaml(paths.glossary) or {}
        return cls(dirname, config, resource_definitions, glossary_dict)

def has_translations(config: dict) -> bool:
    return bool(config.get('translations', None))

def load_yaml(filepath) -> dict:
    with open(filepath, 'r') as file_:
        return yaml.safe_load(file_)

def has_text(filepath) -> bool:
    return os.path.getsize(filepath)!=0

