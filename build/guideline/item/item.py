import os

import frontmatter
import logging

from pathlib import Path
from build.ids import validate_id

def fix_numerical_ids(id):
    if type(id) is int:
        return str(id)
    return id

class Item:
    def __init__(self, id: str, title: str, text: str, filename: str, meta: dict, guideline):
        id = fix_numerical_ids(id)
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
        self.web_rel_path = os.path.join(self.guideline.web_paths.items_rel_dir, self.destination_filename)
        self.html_path = self.guideline.html_paths.make_item_path(self.id)
        self.source_path = os.path.join(self.guideline.repo_paths.items_dir, self.filename)

    def idx(self, resource):
        return self.guideline.resource_definitions_flat[resource].index(self.filename)

    def number(self, resource):
        return self.idx(resource) + 1

    def fallback_summary_text(self):
        text = self.meta.get('checklist', {}).get('text', None)
        text = text or self.text.strip().split('\n')[0].strip()
        if len(text) > 300:
            text = text[:300] + '...'
        text = text or ''
        if text and not text.endswith('.'):
            text += '.'
        return text
    
    def summary_text(self):
        text = self.meta.get('summary', {}).get('text', None)
        text = text or self.fallback_summary_text()
        return text
    
    def summary_title(self):
        text = self.meta.get('summary', {}).get('title', None)
        text = text or self.title
        return text
    
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
            




