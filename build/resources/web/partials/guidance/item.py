import re
import os
import logging

from .sections import Section, text_to_sections
from .readmore import create_collapsible

from build.guideline.glossary import add_glossary_to_string, wrap_string_with_span

INDEX_REGEX = re.compile(r'^\d+[a-z]?\b')
SELF_LINK_REGEX = re.compile(r'\[(?P<text>.+)\]\(\.?\)')

class Item:
    def __init__(self, item, index, guideline):
        self.id = item.id
        self.readmore_id = f"{self.id}-collapsible"
        self.giscus_rel_path = item.giscus_rel_path
        self.text = item.text
        self.index = index
        self.title = item.title
        # index_at_start = INDEX_REGEX.search(self.title)
        # if index_at_start:
        #     self.index = index_at_start.group() #FIXME code smell?
        #     self.title = INDEX_REGEX.sub('', self.title).strip('. ')
        # self.guideline = guideline
        # sections = list(text_to_sections(self.text, self.id))
        # for section in sections:
        #     section.body = self.add_definitions(section.body)
        # if not sections:
        #     logging.warning(f'Item has no body: {guideline.id}, {item.id}')
        # self.sections = sections
        # body_section = sections.pop(0)
        # self.body = self.create_body(body_section)
        # self.body = self.replace_readmore_links(self.body)
        # readmore_sections = sections
        # if readmore_sections:
        #     self.has_readmore = True
        #     title_section = readmore_sections.pop(0)
        #     assert not(title_section.body), item.id
        #     assert title_section.heading
        #     self.readmore_title = title_section.heading
        # else:
        #     self.has_readmore = False
        # self.readmore = create_collapsible(readmore_sections, self)
        # self.md = TEMPLATE.format(item=self).strip()
        
    # def replace_readmore_links(self, body: str) -> str:
    #     links = SELF_LINK_REGEX.finditer(body)
    #     links = list(links)
    #     links = reversed(links)
    #     for idx, link in enumerate(links):
    #         text = link.groupdict()['text']
    #         section = next((section for section in self.sections if section.heading==text), None)
    #         if not section:
    #             logging.warning(f'Item Read More section missing: {self.guideline.id}, {self.id}, {text}')
    #             continue
    #         new_link = f"{text} (see [note](./{section.id}){{.footnote-ref .link-to-collapsible data-target={self.readmore_id} id='note-{self.index}-{idx}' role='doc-noteref' aria-expanded='false'}})"
    #         body = body[:link.start()] + new_link + body[link.end():]
    #     return body

#     def create_body(self, section: Section) -> str:
#         texts = [section.heading, section.body]
#         texts = [text for text in texts if text]
#         text = '\n\n'.join(texts)
#         return text
    
#     def create_web(self) -> str:
#         return self.md

#     def add_definitions(self, string):
#         return add_glossary_to_string(string, self.guideline.glossary_dict, wrap_string_with_span)
    

# TEMPLATE = \
# """::: {{.grid id="{item.id}"}}
# ::: {{.g-col-9}}
# #### {item.index}. {item.title}
# :::
# ::: {{.g-col-3}}
# ::: {{.section .chat-button}}
# <a class="btn btn-outline-secondary" title="Discuss or give feedback on this item" href="{item.giscus_rel_path}" target="_blank"><i class="bi-chat-quote chat-icon"></i></a>
# :::
# :::
# :::

# {item.body}

# {item.readmore}"""


class ItemGroupHeading:
    def __init__(self, text):
        self.body = text
    
    def create_web(self) -> str:
        return f'### {self.body}'