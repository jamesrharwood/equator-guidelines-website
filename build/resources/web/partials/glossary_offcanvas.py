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
        # template = TEMPLATE.replace('{id}', id_)
        # template = template.replace('{header}', header)
        # template = template.replace('{body}', body)
        divs.append(div)
    text = '\n'.join(divs)
    return text

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'glossary_offcanvas.html')
TEMPLATE = file.load_string(TEMPLATE_PATH)

def create_default_glossary_html():
    html = create_html(glossary_default)
    file.save_string(html, 'offcanvas.html')

create_default_glossary_html()