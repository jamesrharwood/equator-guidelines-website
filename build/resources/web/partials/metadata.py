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
    'search': True,
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
    },
    'license': 'Most of the reporting guidelines and checklists on this website were originally published under permissive licenses that allowed their reuse. Some were published with propriety licenses, where copyright is held by the publisher and/or original authors. The original content of the reporting checklists and explanation pages on this website were drawn from these publications with knowledge and permission from the reporting guideline authors, and subsequently revised in response to feedback and evidence from research as part of an ongoing scholarly dialogue about how best to disseminate reporting guidance. The UK EQUATOR Centre makes no copyright claims over reporting guideline content. Our use of copyrighted content on this website falls under fair use guidelines.'
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
        article_key = 'development'
        citation = self.get('articles', {}).get(article_key, None) 
        #TODO switching to development so all RGs have valid citation info
        if citation:
            self.guideline.config['articles'].pop(article_key)
            for field in ['issued', 'accessed']:
                data = adjust_date_field(citation.get(field, None))
                citation.update({field: data})

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
        assert type(bibs) is list, f'Bibliography is loaded as a {type(bibs)}'
        self.set('bibliography', bibs)

    def set_paths(self):
        html_paths = {k: v for k, v in self.guideline.html_paths.__dict__.items() if type(v) is str}
        qmd_paths = {k: v for k, v in self.guideline.web_paths.__dict__.items() if type(v) is str}
        paths = {
            'html': html_paths,
            'qmd': qmd_paths
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

def adjust_date_field(date_list):
    if not date_list:
        return ''
    data = date_list[0]
    return f"{data['month']}/{data.get('day', '')}/{data['year']}"