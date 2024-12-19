import os
import yaml

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
         self.item(f'About {self.guideline.short_name}', self.guideline.web_paths.index),
         self.item('**Summary of guidance**', self.guideline.web_paths.summary),
         self.section('**Full guidance**', self.guidance_contents()),
         self.item('Writing guide', self.guideline.web_paths.writing_guide),
         self.item('Checklist', self.guideline.web_paths.checklist),
         self.item('FAQs', self.guideline.web_paths.faqs)
      ]
   
   def guidance_contents(self):
      # might need to turn this into a recursive func to handle multi layer guidelines
      contents = []
      for dict_ in self.guideline.resource_definitions['web']:
         for title in dict_.keys():
            items = [self.guideline_item(file_) for file_ in dict_[title]]
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
         text = f'{item.title}',
         href = item.web_path
      )
   
   def get_yml(self):
      with open(sidebars_path, 'r') as file_:
         yml = yaml.safe_load(file_)
      return yml
   
   def save_yml(self, yml):
      with open(sidebars_path, 'w') as file_:
         yaml.safe_dump(yml, file_)

   def update_yml(self):
      yml = self.get_yml()
      sidebars = yml['website']['sidebar']
      existing = next((sidebar for sidebar in sidebars if sidebar['id']==self.id), None)
      if existing:
         sidebars.remove(existing)
      sidebars.append(self.create())
      yml['website']['sidebar'] = sidebars
      return yml
   
   def save(self):
      yml = self.update_yml()
      self.save_yml(yml)


