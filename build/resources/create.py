from .web.create import create as create_web
from .bibliography import create as create_bibliography
from .checklist import create as create_checklist
from .writing_guide import create as create_writing_guide

import logging 

strategies = {
    'web': create_web,
    'checklist': create_checklist,
    # 'writing_guide': create_writing_guide,
}

def create_resources(guideline):
    print("Creating web resource: "+guideline.dirname)
    create_bibliography(guideline)
    for key in guideline.resource_definitions.keys():
        if key not in strategies.keys():
            logging.warning(f'Resource {key} for guideline {guideline.id} not valid resource.')
            continue
        strategies[key](guideline)
