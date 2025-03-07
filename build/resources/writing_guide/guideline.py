from build.guideline.guideline import Guideline as Base

from .item import Item

class Guideline(Base):
    item_class = Item

    def create_writing_guide(self):
        texts = list(self.yield_texts())
        texts = [text.replace('\n', '\n\n') for text in texts]
        return '\n\n'.join(texts)

    def yield_texts(self):
        for element in self.resource_definitions['writing_guide']:
            yield from self.yield_resource_element(element, level=1)

    def yield_resource_element(self, element, level):
        # will choose the yield strategy depending on string or list 
        if type(element) is dict:
            yield from self.yield_from_dict(element, level)
        if type(element) is str:
            yield from self.yield_from_filename(element, level)
    
    def yield_from_dict(self, dict, level):
        for key in dict.keys():
            decorator = '#' * level
            yield f"{decorator} {key}"
            for value in dict[key]:
                yield from self.yield_resource_element(value, level+1)

    def yield_from_filename(self, filename, level):
        item = self.get_item_from_filename(filename)
        decorator = '#' * level
        text = f'::: {{.callout-tip title="Things To Consider" icon=false}}\n\n{item.text}\n\n:::'
        yield f"{decorator} {item.title_hyperlinked}\n\n{text}" # type: ignore
        yield "<br>\n\n* Make notes here\n* ...\n* ...\n\n<br>"



    
   