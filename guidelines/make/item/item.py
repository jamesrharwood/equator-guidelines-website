from .sections import Section, text_to_sections
from .readmore import create_collapsible

TEMPLATE = \
"""::: {{.grid id="{id}"}}
::: {{.g-col-9}}
#### {idx}. {title}
:::
::: {{.g-col-3}}
::: {{.section .chat-button}}
[<i class="bi-chat-right-text" data-bs-toggle="offcanvas" href="#offcanvasChat" aria-controls="offcanvasChat" role="button"></i>]{{.btn}}
:::
:::
:::

{body}

{readmore}"""

class Item:
    def __init__(self, id: str, title: str, text: str, index: int):
        self.id = id
        self.title = title
        self.text = text
        self.index = index
        sections = list(text_to_sections(text, self.index))
        body_section = sections[0]
        readmore_sections = sections[1:]
        self.body = self.create_body(body_section)
        self.readmore = create_collapsible(readmore_sections)
        self.md = TEMPLATE.format(
            id=self.id, 
            idx=self.index,
            title=self.title,
            body=self.body,
            readmore=self.readmore
        ).strip()

    def create_body(self, section: Section) -> str:
        texts = [section.heading, section.body]
        texts = [text for text in texts if text]
        text = '\n\n'.join(texts)
        return text




