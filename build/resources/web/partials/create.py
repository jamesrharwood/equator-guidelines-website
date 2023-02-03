from . import metadata, doi, translations, use_for, not_use_for, related_resources, download_resources,\
    guidance, glossary_offcanvas, how_to_use, why_use

class Partial:
    def __init__(self, module, required_if: str|None):
        self.module = module
        self.required_if = required_if
    
    def required_by_guideline(self, guideline):
        if self.required_if is None:
            return True
        return bool(getattr(guideline, self.required_if))
    
    def create_web(self, guideline):
        return self.module.create_web(guideline)

PARTIALS = [
    Partial(metadata, None),
    Partial(doi, None),
    Partial(translations, 'has_translations'),
    Partial(why_use, None),
    Partial(use_for, None),
    Partial(not_use_for, 'has_not_use_for'),
    Partial(related_resources, 'has_related_resources'),
    Partial(how_to_use, None),
    Partial(download_resources, None),
    Partial(guidance, None),
    Partial(glossary_offcanvas, 'glossary_dict')
]  