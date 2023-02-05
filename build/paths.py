import os
from pathlib import Path

root_path = os.path.dirname(os.path.abspath(__file__))
root_path = Path(root_path).parent.absolute()

def join(*args):
    return os.path.join(*args)

class RepoPaths:
    parent_dir = os.path.join(root_path, 'guideline_repos')
    partials_dirname = 'partials'

    def __init__(self, dirname):
        self.dir = join(self.parent_dir, dirname)
        self.config = join(self.dir, 'config.yml')
        self.items_dir = join(self.dir, 'items')
        self.partials_dir = join(self.dir, self.partials_dirname)
        self.use_for = join(self.partials_dir, 'use_for.md')
        self.not_use_for = join(self.partials_dir, 'not_use_for.md')
        self.related_resources = join(self.partials_dir, 'related_resources.md')
        self.resource_definitions = join(self.dir, 'resource_definitions.yml')
        self.guidance = join(self.partials_dir, 'guidance.md')
        self.glossary = join(self.dir, 'glossary.yml')
        self.glossary_offcanvas = join(self.partials_dir, 'glossary_offcanvas.html')
        self.metadata = join(self.dir, '_metadata.yml')
        self.why_use = join(self.partials_dir, 'why_use.md')
        self.how_to_use = join(self.partials_dir, 'how_to_use.md')
    
    def item(self, filename):
        return join(self.items_dir, filename)
    
class DestinationPaths(RepoPaths):
    parent_dir = os.path.join(root_path, 'guidelines')

    def __init__(self, dirname):
        super().__init__(dirname)
        self.index = join(self.dir, 'index.qmd')

class RelativeDestinationPaths(DestinationPaths):
    parent_dir = ''

    def __init__(self, dirname):
        super().__init__('')
        self.index = join(self.dir, 'index.qmd')
