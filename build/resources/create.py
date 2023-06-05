from .web.create import create as create_web

def create_resources(guideline):
    print("Creating web resource: "+guideline.dirname)
    create_web(guideline)