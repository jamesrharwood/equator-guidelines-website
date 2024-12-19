import os

import frontmatter
import logging

from pathlib import Path
from build.ids import validate_id

class Item:
    def __init__(self, id: str, title: str, text: str, filename: str, meta: dict, guideline):
        validate_id(id)
        self.id = id
        self.title = title
        self.text = text
        self.filename = filename
        self.meta = meta
        self.guideline=guideline
        self.giscus_path = os.path.join(guideline.destination_paths.giscus_dir, f'{self.id}.qmd')
        self.giscus_rel_path = os.path.join(guideline.destination_paths.giscus_rel_dir, f'{self.id}.qmd')
        self.destination_filename = self.id + '.qmd'
        self.web_path = os.path.join(self.guideline.web_paths.items_dir, self.destination_filename)
        self.source_path = os.path.join(self.guideline.repo_paths.items_dir, self.filename)

    def idx(self, resource):
        return self.guideline.resource_definitions_flat[resource].index(self.filename)

    def number(self, resource):
        return self.idx(resource) + 1

    def checklist_text(self):
        return self.meta.get('checklist', None) or \
        self.text.strip().split('\n')[0].strip() + '...' or \
        'Summary'
    
    @classmethod
    def from_filepath(cls, filepath, guideline):
        try:
            md = frontmatter.load(filepath)
        except Exception as e:
            logging.warning(f'Error loading markdown from file: {filepath}')
            raise e
        meta = md.metadata
        filename = Path(filepath).name
        return cls(
            id=meta['id'],
            title=meta['title'],
            text=md.content,
            filename=filename,
            meta=meta,
            guideline=guideline,
        )
            




