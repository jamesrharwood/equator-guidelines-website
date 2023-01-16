from .sections import Section  

def create_collapsible(sections: list[Section]) -> str:
    if not sections: 
        return ''
    if len(sections) == 1:
        return create_collapsible_simple(sections[0])
    else:
        return create_collapsible_with_toc(sections)

def create_collapsible_simple(section: Section):
    return _collapsible(toc='', body=create_body([section]), back_to_top='')

def create_collapsible_with_toc(sections: list[Section]):
    item_index = sections[0].item_index
    return _collapsible(
        toc=create_toc(sections),
        body=create_body(sections),
        back_to_top=create_back_to_top(item_index)
    )

def _collapsible(toc: str, body: str, back_to_top: str) -> str:
    return f"""::: {{.callout-note appearance="minimal" collapse=true}}

## Read more 

{toc}

{body}

{back_to_top}
:::

"""
def create_back_to_top(item_index):
    return f'[Back to top](#{item_index})"'

def create_toc(sections: list[Section]) -> str:
    toc = "Jump to:\n\n"
    for sec in sections:
        toc += f"* {sec.toc_md}\n"
    return toc

def create_body(sections: list[Section]) -> str:
    body = '\n\n'.join((sec.md for sec in sections))
    return body

