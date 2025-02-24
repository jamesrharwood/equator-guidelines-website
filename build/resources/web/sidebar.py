import os
from build.file import get_yml, save_yml

from build.paths import root_path
sidebars_path = os.path.join(root_path, '_sidebars.yml')

DEFAULT = {
    'search': True,
    'style': 'docked',
    'foreground': 'secondary',
    'collapse-level': 2,
}

class Sidebar:
   def __init__(self, guideline):
      self.guideline = guideline
      self.id = self.guideline.id
      self.sidebar = self.create()

   def create(self):
      dict_ = {'id': self.id}
      dict_.update(DEFAULT)
      dict_.update({'contents': self.contents()})
      return dict_
   
   def contents(self):
      return [
         # self.item('How to use', self.guideline.web_paths.index),
         self.item(f'Overview of {self.guideline.short_name}', self.guideline.web_paths.index),
         # self.item('**Summary of guidance**', self.guideline.web_paths.summary),
         self.section('Full guidance', self.guidance_contents()),
         self.item('Writing guide', self.guideline.web_paths.writing_guide),
         self.item('Checklist', self.guideline.web_paths.checklist),
         self.item('FAQs', self.guideline.web_paths.faqs)
      ]
   
   def guidance_contents(self):
      # might need to turn this into a recursive func to handle multi layer guidelines
      contents = []
      for dict_ in self.guideline.resource_definitions['web']:
         for title in dict_.keys():
            items = []
            for entry in dict_[title]:
               if type(entry) is str:
                  items.append(self.guideline_item(entry))
               elif type(entry is dict):
                  keys = list(entry.keys())
                  assert len(keys)==1
                  key = keys[0]
                  values = entry[key]
                  items.append(self.section(key, [self.guideline_item(v) for v in values]))
            contents.append(self.section(title, items))
      return contents

   def section(self, title, contents, bold=False):
      template = '**{title}**' if bold else '{title}'
      return dict(
         section=template.format(title=title),
         contents=contents
      )

   def item(self, text, href):
      return dict(text=text, href=href)
    
   def guideline_item(self, file_):
      item = next(i for i in self.guideline.items if i.filename==file_)
      return self.item(
         text = f'{item.summary_title()}',
         href = item.web_path
      )

   def update_yml(self):
      yml = get_yml(sidebars_path)
      sidebars = yml['website']['sidebar']
      existing = next((sidebar for sidebar in sidebars if sidebar['id']==self.id), None)
      if existing:
         sidebars.remove(existing)
      sidebars.append(self.create())
      yml['website']['sidebar'] = sidebars
      return yml
   
   def save(self):
      yml = self.update_yml()
      save_yml(sidebars_path, yml)


