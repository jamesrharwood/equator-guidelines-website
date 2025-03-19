from .web.create import create as create_web
from .bibliography import create as create_bibliography
from .checklist import create as create_checklist
from .writing_guide import create as create_writing_guide

def create_resources(guideline):
    print("Creating web resource: "+guideline.dirname)
    create_bibliography(guideline)
    create_checklist(guideline)
    create_writing_guide(guideline)
    create_web(guideline)
