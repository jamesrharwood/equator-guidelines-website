import os

from build import file
from build.guideline.glossary import id_from_index

def create_web(guideline):
    html = create_html(guideline.glossary_dict)
    file.save_string(html, guideline.destination_paths.glossary_offcanvas)
    return f"{{{{< include {guideline.relative_destination_paths.glossary_offcanvas} >}}}}"

def create_html(glossary_dict):
    divs = []
    for idx, tup in enumerate(glossary_dict.items()):
        key, value = tup
        id_ = id_from_index(idx)
        header = key.capitalize()
        div = TEMPLATE.format(id=id_, header=header, body=value)
        divs.append(div)
    html = '\n'.join(divs)
    return html

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'glossary_offcanvas.html')
TEMPLATE = file.load_string(TEMPLATE_PATH)

