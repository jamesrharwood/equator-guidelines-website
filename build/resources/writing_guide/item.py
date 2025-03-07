import re

from build.resources.checklist.item import Item as Base

NUM_ID = re.compile(r'^\d+\w*\.?')
NUM_ALPHA = re.compile(r'^\d+([a-z]+\.?)')
CAPITAL_LETTER = re.compile(r'[A-Z]')

class Item(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = self.meta.get('writing_guide', {}).get('title') or self.title
        self.text = self.meta.get('writing_guide', {}).get('text') or self.text






