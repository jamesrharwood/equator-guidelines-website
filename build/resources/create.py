from .web.create import create as create_web
from .bibliography import create as create_bibliography
from .checklist import create as create_checklist

def create_resources(guideline):
    print("Creating web resource: "+guideline.dirname)
    create_web(guideline)
    create_bibliography(guideline)
    create_checklist(guideline)