from .sections import Section  

def create_collapsible(sections: list[Section], item) -> str:
    if not sections: 
        return ''
    if len(sections) == 1:
        return create_collapsible_simple(sections[0], item)
    else:
        return create_collapsible_with_toc(sections, item)

def create_collapsible_simple(section: Section, item) -> str:
    return _collapsible(toc='', body=create_body([section]), back_to_top='', item=item)

def create_collapsible_with_toc(sections: list[Section], item) -> str:
    item_index = sections[0].item_index
    return _collapsible(
        toc=create_toc(sections),
        body=create_body(sections),
        back_to_top=create_back_to_top(item_index),
        item=item
    )

def _collapsible(toc: str, body: str, back_to_top: str, item) -> str:
    return f"""::: {{#{item.readmore_id} .callout-note appearance="minimal" collapse=true}}

## Justification, examples, and resources

{toc}

{body}

{back_to_top}
:::

"""
def create_back_to_top(item_index):
    return f'[Back to top](#{item_index})'

def create_toc(sections: list[Section]) -> str:
    toc = "Jump to:\n\n"
    for sec in sections:
        toc += f"* {sec.toc_md}\n"
    return toc

def create_body(sections: list[Section]) -> str:
    body = '\n\n'.join((sec.md for sec in sections))
    return body

