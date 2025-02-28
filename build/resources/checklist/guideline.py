from build.guideline.guideline import Guideline as Base

from .item import Item
from .table import ChecklistTable

class Guideline(Base):
    item_class = Item

    @property
    def table(self):
        return ChecklistTable(self)

    def get_table_markdown(self):
        return self.table.get_markdown()
    
    
    


