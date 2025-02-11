import os

from dataclasses import dataclass, field

import yaml

from .item import Item
from .glossary import transform_dict as transform_glossary
from .glossary_default import glossary_default
from build.paths import RepoPaths, DestinationPaths, RelativeDestinationPaths, WebPaths
from build.resources import create_resources
from build.ids import validate_id

# This could be better as a normal class, not dataclass

@dataclass
class Guideline:
    dirname: str
    config: dict
    resource_definitions: dict
    resource_definitions_flat: dict = field(init=False)
    glossary_dict: dict
    glossary_default_dict: dict
    repo_paths: RepoPaths = field(init=False)
    destination_paths: DestinationPaths = field(init=False)
    has_translations: bool = field(init=False)
    has_not_use_for: bool = field(init=False)
    has_related_resources: bool = field(init=False)
    has_why_use: bool = field(init=False)
    has_how_to_use: bool = field(init=False)
    id: str = field(init=False)
    doi: str = field(init=False)
    translations: list[dict] = field(init=False)
    data_repo: str = field(init=False)
    has_data_repo: bool = field(init=False)
    has_open_e_and_e: bool = field(init=False)

    def create_resources(self):
        self.create_folder()
        create_resources(self)
    
    def create_folder(self):
        paths = [
            self.destination_paths.dir,
            self.destination_paths.partials_dir,
            self.destination_paths.giscus_dir,
            self.destination_paths.items_dir,
        ]
        for path in paths:
            if not os.path.exists(path): # type: ignore
                os.makedirs(path) # type: ignore
    
    def __post_init__(self):
        self.repo_paths = RepoPaths(self.dirname)
        self.destination_paths = DestinationPaths(self.dirname)
        self.relative_destination_paths = RelativeDestinationPaths('')
        self.web_paths = WebPaths(self.dirname)
        self.doi = self.config['doi']
        self.translations = self.config.get('translations', [])
        id = self.config['id']
        validate_id(id)
        self.id = id
        self.has_translations = has_translations(self.config)
        self.has_not_use_for = has_text(self.repo_paths.not_use_for)
        self.has_related_resources=has_text(self.repo_paths.related_resources)
        self.items = list(self.load_items())
        self.has_how_to_use=has_text(self.repo_paths.how_to_use)
        self.has_why_use=has_text(self.repo_paths.why_use)
        self.data_repo = self.config.get('data-repo', None)
        self.has_data_repo = bool(self.data_repo)
        self.resource_definitions_flat = self.flatten_resource_definitions()
        self.has_open_e_and_e = self.config['open-e-and-e']
        self.short_name = self.config.get('acronym', 'this guideline')
    
    def load_items(self):
        item_dir = self.repo_paths.items_dir
        for filename in os.listdir(item_dir):
            path = os.path.join(item_dir, filename)
            yield Item.from_filepath(path, self)

    def flatten_resource_definitions(self):
        flat_definitions = {}
        for resource_name, definition in self.resource_definitions.items():
            filenames = []
            for dict_ in definition:
                for list_ in dict_.values():
                    filenames.extend(list_)
            flat_definitions[resource_name] = filenames
        return flat_definitions

    @classmethod
    def create(cls, dirname: str):
        paths = RepoPaths(dirname)
        config = load_yaml(paths.config)
        resource_definitions = load_yaml(paths.resource_definitions)
        glossary_dict = load_yaml(paths.glossary) or {}
        glossary_dict = transform_glossary(glossary_dict)
        glossary_default_dict = transform_glossary(glossary_default)
        return cls(dirname, config, resource_definitions, glossary_dict, glossary_default_dict)

def has_translations(config: dict) -> bool:
    return bool(config.get('translations', None))

def load_yaml(filepath) -> dict:
    with open(filepath, 'r') as file_:
        return yaml.safe_load(file_)

def has_text(filepath) -> bool:
    return os.path.getsize(filepath)!=0

