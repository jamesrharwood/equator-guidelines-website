import os

import frontmatter
import logging

from pathlib import Path

from ..glossary import add_glossary_to_string

class Item:
    def __init__(self, id: str, title: str, text: str, filename: str, guideline):
        self.id = id
        self.title = title
        self.text = text
        self.filename = filename
        self.guideline=guideline
        self.giscus_path = os.path.join(guideline.destination_paths.giscus_dir, f'{self.id}.qmd')
        self.giscus_rel_path = os.path.join(guideline.destination_paths.giscus_rel_dir, f'{self.id}.qmd')

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
            guideline=guideline,
        )
            




