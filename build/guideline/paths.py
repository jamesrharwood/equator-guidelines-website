import os
from pathlib import Path

root_path = os.path.dirname(os.path.realpath(__file__))
root_path = Path(root_path).parent.parent.absolute()

def join(*args):
    return os.path.join(*args)

class RepoPaths:
    dir_path = os.path.join(root_path, 'guideline_repos')

    def __init__(self, dirname):
        self.dir = join(self.dir_path, dirname)
        self.config = join(self.dir, 'config.yml')
        self.items_dir = join(self.dir, 'items')
        self.use_for = join(self.dir, 'use_for.md')
        self.not_use_for = join(self.dir, 'not_use_for.md')
        self.related_resources = join(self.dir, 'related_resources.md')
        self.resource_definitions_dir = join(self.dir, 'resource_definitions')
        self.guidance_definition = join(self.resource_definitions_dir, 'guidance.yml')
    
    def item(self, filename):
        return join(self.items_dir, filename)
    
class DestinationPaths(RepoPaths):
    dir_path = os.path.join(root_path, 'guidelines')

    def __init__(self, dirname):
        self.index = join(self.dir_path, 'index.qmd')
        super().__init__(dirname)