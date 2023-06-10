from . import giscus, how_to_cite, metadata, doi, translations, use_for, not_use_for, related_resources, download_resources,\
    guidance, glossary_offcanvas, how_to_use, why_use, ready_to_start, faqs, read_time

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
    #Partial(translations, 'has_translations'),
    Partial(why_use, 'has_why_use'),
    Partial(how_to_use, 'has_how_to_use'),
    Partial(read_time, None),
    Partial(use_for, None),
    Partial(not_use_for, 'has_not_use_for'),
    Partial(related_resources, 'has_related_resources'),
    Partial(guidance, None),
    Partial(ready_to_start, None),
    Partial(how_to_cite, None),
    Partial(faqs, None),
    Partial(giscus, 'has_data_repo'),
    Partial(glossary_offcanvas, 'glossary_dict'),
]  