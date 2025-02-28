import re

from build.guideline.item import Item as Base

NUM_ID = re.compile(r'^\d+\w*\.?')
NUM_ALPHA = re.compile(r'^\d+([a-z]+\.?)')
CAPITAL_LETTER = re.compile(r'[A-Z]')

class Item(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        title = self.meta.get('checklist', {}).get('title', None) or \
            self.summary_title()
        self.title = NUM_ID.sub('', title).strip()
        self.num_ids = self.get_num_ids(title)
        self.text = self.meta.get('checklist', {}).get('text', None) or \
            self.summary_text()
        self.title_hyperlinked = f'[{title}]({self.html_path})'

    def get_num_ids(self, title):
        num_ids = ''
        num_ids = NUM_ID.search(title)
        if num_ids:
            num_ids = num_ids.group()
            alpha_ids = NUM_ALPHA.search(num_ids)
            if alpha_ids:
                alpha_ids = alpha_ids.groups()[0]
                if not alpha_ids.endswith('.'):
                    alpha_ids += '.'
                num_ids = num_ids.replace(
                alpha_ids,
                f'. {alpha_ids}'
            )
        return num_ids





