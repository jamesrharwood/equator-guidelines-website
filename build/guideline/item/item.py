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
    text_limit = 300

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

    def summary_text(self):
        text = self.meta.get('summary', {}).get('text', '').strip()
        text = text or self.fallback_summary_text()
        return text
    
    def summary_title(self):
        text = self.meta.get('summary', {}).get('title', '').strip()
        text = text or self.title
        return text

    def fallback_summary_text(self):
        text = self.meta.get('checklist', {}).get('text', '').strip()
        if not text:
            text = self.first_section()
            text = self.truncate(text, 300)
            text = self.add_stop(text)
        return text
    
    def first_section(self):
        text = ''
        texts = self.text.strip().split('\n')
        heading_count = 0
        for t in texts:
            if t.strip().startswith('#'):
                heading_count += 1
            else:
                text += '\n' + t
            if heading_count > 1:
                break
        text = text.strip()
        return text

    def truncate(self, text, limit=None):
        limit = limit or self.text_limit
        if not limit:
            return text
        if len(text) > limit:
            text = text[:limit] + '...'
        return text
    
    def add_stop(self, text):
        if text and text[-1] not in ['.', '?']:
            text += '.'
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
            




