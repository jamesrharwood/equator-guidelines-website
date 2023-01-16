import frontmatter

from pathlib import Path

from ..glossary import add_glossary_to_string

class Item:
    def __init__(self, id: str, title: str, text: str, filename: str):
        self.id = id
        self.title = title
        self.text = text
        self.filename = filename

    @classmethod
    def from_filepath(cls, filepath):
        md = frontmatter.load(filepath)
        meta = md.metadata
        filename = Path(filepath).name
        return cls(
            id=meta['id'],
            title=meta['title'],
            text=md.content,
            filename=filename,
        )
            




