import os

from dataclasses import dataclass

import yaml

from .item import Item
from .paths import Paths

@dataclass
class Guideline:
    paths: Paths
    config: dict
    has_translations: bool
    has_not_use_for: bool
    has_related_resources: bool

def create(dirname:str):
    paths = Paths(dirname)
    config = load_yaml(paths.config)

    return Guideline(
        paths=paths,
        config=config,
        has_translations=has_translations(config),
        has_not_use_for=has_text(paths.not_use_for),
        has_related_resources=has_text(paths.related_resources)
    )

def has_translations(config: dict) -> bool:
    return bool(config['translations'])

def load_yaml(filepath):
    with open(filepath, 'r') as file_:
        return yaml.safe_load(file_)

def has_text(filepath):
    return os.path.getsize(filepath)!=0