from urllib.parse import quote

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

    @property
    def utm_campaign(self):
        campaign = self.version.replace(' ', '_')
        campaign = campaign.replace('-', '_')
        campaign = campaign.replace('.', '_')
        campaign = quote(campaign)
        return campaign

    
    
    


