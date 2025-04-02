import os
from pathlib import Path
import yaml

root_path = os.path.dirname(os.path.abspath(__file__))
root_path = Path(root_path).parent.absolute()
GUIDELINES_DIR = 'guidelines'
ITEMS_DIR = 'items'

with open('_quarto.yml', 'r') as file_:
    metadata = yaml.safe_load(file_)

def join(*args):
    return os.path.join(*args)

class Paths:
    def __init__(self, dirname):
        self.repo = RepoPaths(dirname)
        self.destination = DestinationPaths(dirname)
        self.web_files = WebPaths(dirname)
        self.html = HtmlPaths(dirname)

class RepoPaths:
    parent_dir = os.path.join(root_path, 'guideline_repos')
    partials_dirname = 'partials'

    def __init__(self, dirname):
        self.dir = join(self.parent_dir, dirname)
        self.config = join(self.dir, 'config.yml')
        self.items_dir = join(self.dir, ITEMS_DIR)
        self.items_rel_dir = ITEMS_DIR
        self.partials_dir = join(self.dir, self.partials_dirname)
        self.use_for = join(self.partials_dir, 'use_for.md')
        self.faqs = join(self.partials_dir, 'faqs.md')
        self.not_use_for = join(self.partials_dir, 'not_use_for.md')
        self.related_resources = join(self.partials_dir, 'related_resources.md')
        self.resource_definitions = join(self.dir, 'resource_definitions.yml')
        self.guidance = join(self.partials_dir, 'guidance.md')
        self.glossary = join(self.dir, 'glossary.yml')
        self.glossary_offcanvas = join(self.partials_dir, 'glossary_offcanvas.html')
        self.metadata = join(self.dir, '_metadata.yml')
        self.why_use = join(self.partials_dir, 'why_use.md')
        self.how_to_use = join(self.partials_dir, 'how_to_use.md')
        self.how_to_cite = join(self.partials_dir, 'how_to_cite.md')
        self.item_order = join(self.partials_dir, 'item_order.md')
        self.author_bios = join(self.partials_dir, 'author_bios.md')
        self.development = join(self.partials_dir, 'development.md')
        self.bibliographies = join(self.dir, 'bibliographies')
        self.uploads = join(self.dir, 'uploads')

    def item(self, filename):
        return join(self.items_dir, filename)
    
class DestinationPaths(RepoPaths):
    parent_dir = os.path.join(root_path, GUIDELINES_DIR)
    giscus_dirname = 'discussion'

    def __init__(self, dirname):
        super().__init__(dirname)
        self.index = join(self.dir, 'index.qmd')
        self.giscus_dir = join(self.dir, self.giscus_dirname)
        self.giscus_rel_dir = self.giscus_dir.replace(str(root_path), '')
        self.checklist = join(self.dir, f'{dirname}-checklist.qmd')
        self.writing_guide = join(self.dir, f'{dirname}-writing-guide.qmd')

class RelativeDestinationPaths(DestinationPaths):
    parent_dir = ''

    def __init__(self, dirname):
        super().__init__('')
        self.index = join(self.dir, 'index.qmd')

class WebPaths(DestinationPaths):
    parent_dir = GUIDELINES_DIR

    def __init__(self, dirname):
        super().__init__(dirname)
        self.index = join(self.dir, 'index.qmd')
        self.summary = join(self.dir, 'summary.qmd')
        self.items_dir = self.items_dir
        self.faqs = join(self.dir, 'faqs.qmd')
        self.faqs_partial = join(self.partials_dir, 'faqs.md')
        self.about_reporting_guidelines = str(Path('about', 'reporting-guidelines.qmd'))
        self.about_writing_guides = str(Path('about', 'writing-using-reporting-guidelines.qmd'))
        self.applicability = self.index + '?#applicability' #TODO replace with a constant
        self.training = 'training.qmd'
        self.checklist = str(Path(self.checklist).with_suffix('.docx'))
        self.writing_guide = str(Path(self.writing_guide).with_suffix('.docx'))

class HtmlPaths():
    # consider refactoring this to make it Document paths: paths to use in Docx files
    # Because otherwise github pages adds its domain to the paths again
    URL = metadata['website']['site-url']
    def __init__(self, dirname):
        self.web_paths = WebPaths(dirname)
        self.applicability = self.index + '?#applicability' #TODO replace with a constant
        self.checklist = self.make_path(self.web_paths.checklist, suffix='.docx')
        self.writing_guide = self.make_path(self.web_paths.writing_guide, suffix='.docx')
        self.about_reporting_guidelines = self.make_path(self.web_paths.about_reporting_guidelines)
        self.about_writing_guides = self.make_path(self.web_paths.about_writing_guides)
        self.training = self.make_path(self.web_paths.training)
        self.full_guideline = self.index
        self.home_page = self.URL

    def make_item_path(self, filename):
        return self.make_path(self.web_paths.items_dir, filename)
    
    def make_path(self, *paths, suffix='.html'):
        assert suffix.startswith('.')
        return str(Path(self.URL, *paths).with_suffix(suffix))
    
    def __getattr__(self, attr):
        val = getattr(self.web_paths, attr)
        if not type(val) is str:
            raise Exception('Attempting to create a html path from a web_path that is not a string for attribute: ', attr)
        if val.endswith('qmd'):
            val = self.make_path(val)
        return val


