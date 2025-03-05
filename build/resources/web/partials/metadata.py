from build.file import save_yml
from copy import copy

def create_web(guideline):
    metadata = create_metadata(guideline)
    save_yml(guideline.destination_paths.metadata, metadata)
    return ''

DEFAULT = {
    'css': [ 
        '../../css/styles.css',
        '../../css/index.css',
        '../../css/guidelines.css',
        '../../css/styles2.css',
    ],
    'appendix-style': 'default',
    'search': False,
    'footer': 'none',
    'appendix-cite-as': False,
    'google-scholar': True,
    'format': {
        'html': {
            'include-after-body': 'partials/glossary_offcanvas.html',
        },
    },
    'project': {
        'render': [
            '*glossary*',
            '*.qmd',
            '*.md',
        ]
    }
}

CONTAINER =   {
    'container-title': 'The EQUATOR Network guideline dissemination platform',
    'container-author': [ 
        {'name': 'James Harwood'},
        {'name': 'Charlotte Albury'},
        {'name': 'Jennifer de Beyer'},
        {'name': 'Michael Schlüssel'},
        {'name': 'Caroline Struthers'},
        {'name': 'Gary Collins'},
    ]
}
CITATION_DEFAULTS = {
    'type': 'webpage',
}

class MetadataCreator():
    def __init__(self, guideline):
        self.guideline = guideline
        self.metadata = copy(DEFAULT)
    
    def set(self, key, value):
        self.metadata.update({key: value})

    def copy(self, attr):
        value = self.guideline.config[attr]
        self.set(attr, value)
    
    def get(self, attr, default=None):
        return self.guideline.config.get(attr, default)
    
    def set_citation(self):
        citation = self.get('articles', {}).get('citation', None)
        if citation:
            self.guideline.config['articles'].pop('citation')
        if not citation:
            citation = self.guideline.config.get('citation', {})
            citation.update(CONTAINER)
            citation.update(CITATION_DEFAULTS)
            citation.update({'doi': self.get('doi')})
            citation.update({'version': self.get('version')})
            citation.update({'title': self.get('title')})
            citation.update({'author': self.get('authors')})
        self.set('citation', citation)
        self.set('appendix-cite-as', 'display')

    def set_translation(self):
        translations = self.get('translations', [])
        translations = [f'[{t["language"]}]({t["url"]})' for t in translations]
        if len(translations) > 1:
            translations = '\n\n' + '\n* '.join(translations) + '\n\n'
        else:
            translations = translations[0] if translations else ''
        self.set('translations', translations)  

    def set_items(self):
        items = {}
        for item in self.guideline.items:
            items.update(
                {item.id: 
                {
                    'title': item.title,
                    'web_path': '/'+item.web_path
                }
            })
        self.set('items', items)

    def set_authors(self):
        authors = []
        for auth in self.get('authors', []):
            if type(auth) is str:
                authors.append(auth)
            elif type(auth) is dict:
                if 'literal' in auth.keys():
                    authors.append(auth['literal'])
                else:
                    authors.append(f"{auth['given']} {auth['family']}")
        self.set('author_list', ',\n'.join(authors))

    def set_bibliographies(self):
        bibs = self.get('bibliography', [])
        assert type(bibs) is list
        self.set('bibliography', bibs)

    def set_paths(self):
        paths = {
            'html': {
                'applicability': self.guideline.html_paths.applicability,
                'full_guideline': self.guideline.html_paths.index,
                'writing_guide': self.guideline.html_paths.writing_guide,
                'checklist': self.guideline.html_paths.checklist,
                'home_page': self.guideline.html_paths.URL,
                'about_writing_guides': self.guideline.html_paths.about_writing_guides,
                'about_reporting_guidelines': self.guideline.html_paths.about_reporting_guidelines,
            }
        }
        self.set('paths', paths)

    def create(self):
        self.copy('title')
        self.copy('acronym')
        self.copy('id')
        self.copy('acronym-definition')
        self.copy('journal-endorsement-count')
        self.copy('articles')
        self.copy('version')
        self.copy('for-writing')
        self.set_paths()
        self.set_citation()
        self.set_translation()
        self.set_items()
        self.set_authors()
        self.set_bibliographies()
        return self.metadata

def create_metadata(guideline):
    metadata = MetadataCreator(guideline)
    return metadata.create()


