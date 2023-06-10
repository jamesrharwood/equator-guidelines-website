from .item import Item, ItemGroupHeading

from typing import Iterable, Protocol 

class ItemProtocol(Protocol):
    body: str 

    def create_web(self) -> str:
        ...

class Guidance:
    def __init__(self, guideline):
        self.guideline = guideline
        self.index = None
    
    def create_web(self):
        guidance = '\n\n'.join(list(self.create_web_texts()))
        return guidance

    def create_web_texts(self) -> Iterable[str]:
        items = self.items_for_resource('web')
        for item in items:
            yield item.create_web()
       
    def items_for_resource(self, resource:str) -> Iterable[ItemProtocol]:
        self.index = 1
        contents_list = self.guideline.resource_definitions[resource]
        for item in self.items_generator(contents_list):
            yield item
        self.index = None
   
    def items_generator(self, contents) -> Iterable[ItemProtocol]:
        generator = self.get_generator(contents)
        for item in generator:
            yield item

    def get_generator(self, contents):
        type_ = type(contents)
        generators = {
            str: self._generate_item,
            list: self._generate_items_from_list,
            dict: self._generate_items_from_dict,
        }
        generator = generators[type_]
        return generator(contents)

    def _generate_items_from_list(self, contents_list: list) -> Iterable[ItemProtocol]:
        for element in contents_list:
            for item in self.items_generator(element):
                yield item
         
    def _generate_items_from_dict(self, collection: dict) -> Iterable[ItemProtocol]:
        heading = list(collection.keys())[0]      
        contents_list = collection[heading]
        heading = ItemGroupHeading(heading)
        yield heading
        for item in self.items_generator(contents_list):
            yield item
        
    def _generate_item(self, filename):
        try:
            item = next(item for item in self.guideline.items if item.filename==filename)
        except StopIteration:
            raise Exception(f'{self.guideline.id} has no item with filename {filename}. Items are:\n\n{[item.filename for item in self.guideline.items]}')
        item = Item(item, self.index, self.guideline)
        self.index += 1 # type: ignore
        yield item
    
    def get_reading_time(self, resource):
        words = 0
        items = self.items_for_resource(resource)
        for item in items:
            words += len(item.body.split())
        reading_time = int(words/183) # apparently we read 183 words per minute
        return reading_time