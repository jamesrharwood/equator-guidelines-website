import os
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = Path(dir_path).parent.parent.absolute()
dir_path = os.path.join(dir_path, 'guidelines')

def join(*args):
    return os.path.join(*args)

class Paths:
    def __init__(self, dirname):
        self.dir = join(dir_path, dirname)
        self.config = join(self.dir, 'config.yml')
        self.items_dir = join(self.dir, 'items')
        self.use_for = join(self.dir, 'use_for.md')
        self.not_use_for = join(self.dir, 'not_use_for.md')
        self.related_resources = join(self.dir, 'related_resources.md')
        self.resource_definitions_dir = join(self.dir, 'resource_definitions')
        self.guidance_definition = join(self.resource_definitions_dir, 'guidance.yml')
    
    def item(self, filename):
        return join(self.items_dir, filename)