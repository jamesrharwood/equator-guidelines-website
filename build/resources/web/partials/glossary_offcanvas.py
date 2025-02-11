import os

from build import file
from build.guideline.glossary import glossary_id
from build.guideline.glossary_default import glossary_default

def create_web(guideline):
    html = create_html(guideline.glossary_dict)
    file.save_string(html, guideline.destination_paths.glossary_offcanvas)
    return ''

def create_html(glossary_dict):
    divs = []
    for value in glossary_dict.values():
        id_ = glossary_id(value['id'])
        header = value['title']
        body = value['text']
        div = TEMPLATE.format(id=id_, header=header, body=body)
        divs.append(div)
    html = '\n'.join(divs)
    return html

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'glossary_offcanvas.html')
TEMPLATE = file.load_string(TEMPLATE_PATH)

def create_default_glossary_html():
    divs = []
    for item in glossary_default.values():
        id = glossary_id(item['id'])
        divs.append(TEMPLATE.format(id=id, header=item['title'], body=item['text']))
    html = '\n'.join(divs)
    file.save_string(html, 'offcanvas.html')

create_default_glossary_html()