import re

from typing import Iterator
from dataclasses import dataclass

HEADING_REGEX = re.compile(r'^\s*#+\s*(?P<heading>[^\n]+)(\n+|$)')

@dataclass
class Section:
    heading: str
    index: int
    body: str
    item_index: int

    @property
    def id(self) -> str:
        return f"#sec-{self.item_index}-{self.index}"
    
    #TA The 3 properties below might not belong in Section object as they assume Section knows about expected Read More structure
    @property
    def toc_md(self) -> str:
        return f"[{self.heading}]({self.id})"

    @property
    def body_heading(self) -> str:
        return f"## {self.heading}{{{self.id}}}"
    
    @property
    def md(self) -> str:
        return '\n\n'.join([self.body_heading, self.body])


def text_to_texts(text:str) -> Iterator[str]:
    lines = text.splitlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    if not lines:
        return ''
    snippet = lines[0]
    for line in lines[1:]:
        line = line.strip()
        if not line.strip().startswith('#'):
            snippet += '\n\n' + line
        else:
            yield snippet
            snippet = line
    yield snippet

def text_to_sections(text: str, item_index: int) -> Iterator[Section]:
    texts = text_to_texts(text)
    for idx, text in enumerate(texts):
        yield text_to_section(text, idx, item_index)

def text_to_section(text: str, index: int, item_index: int) -> Section:
    heading_match = HEADING_REGEX.search(text)
    if heading_match:
        heading = heading_match.groupdict()['heading'].strip()
        body = text.replace(heading_match.group(), '')
    else:
        heading = ''
        body = text
    return Section(heading=heading, body=body, index=index, item_index=item_index)

