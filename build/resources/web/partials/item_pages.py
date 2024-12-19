from build.file import copy, load_string

def create_web(guideline):
    for item in guideline.items:
        copy(item.source_path, item.web_path)
    return ''

class Item:
    def __init__(self, item):
        self.item = item
    
    def create_web(self, _):
        text = load_string(self.item.source_path)
        text += f"""\n\n## Discuss this item\n\nVisit this items' [discussion page]({self.item.giscus_rel_path}) to ask questions and give feedback."""
        return text