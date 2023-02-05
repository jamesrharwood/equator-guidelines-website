import re
import logging

from .sections import Section, text_to_sections
from .readmore import create_collapsible

from build.guideline.glossary import add_glossary_to_string, wrap_string_with_span

INDEX_REGEX = re.compile(r'^\d+[a-z]?\b')

class Item:
    def __init__(self, item, index, guideline):
        self.id = item.id
        self.title = item.title
        self.text = item.text
        self.index = index
        index_at_start = INDEX_REGEX.search(self.title)
        if index_at_start:
            self.index = index_at_start.group() #FIXME code smell?
            self.title = INDEX_REGEX.sub('', self.title).strip('. ')
        self.guideline = guideline
        sections = list(text_to_sections(self.text, self.id))
        for section in sections:
            section.body = self.add_definitions(section.body)
        if not sections:
            logging.warn(f'Item has no body: {guideline.id}, {item.id}')
        body_section = sections[0]
        readmore_sections = sections[1:]
        self.body = self.create_body(body_section)
        self.readmore = create_collapsible(readmore_sections)
        self.md = TEMPLATE.format(
            id=self.id, 
            index=self.index,
            title=self.title,
            body=self.body,
            readmore=self.readmore
        ).strip()

    def create_body(self, section: Section) -> str:
        texts = [section.heading, section.body]
        texts = [text for text in texts if text]
        text = '\n\n'.join(texts)
        return text
    
    def create_web(self) -> str:
        return self.md

    def add_definitions(self, string):
        return add_glossary_to_string(string, self.guideline.glossary_dict, wrap_string_with_span)
    

TEMPLATE = \
"""::: {{.grid id="{id}"}}
::: {{.g-col-9}}
#### {index}. {title}
:::
::: {{.g-col-3}}
::: {{.section .chat-button}}
[<i class="bi-chat-right-text" data-bs-toggle="offcanvas" href="#offcanvasChat" aria-controls="offcanvasChat" role="button"></i>]{{.btn}}
:::
:::
:::

{body}

{readmore}"""


class ItemGroupHeading:
    def __init__(self, text):
        self.body = text
    
    def create_web(self) -> str:
        return f'### {self.body}'