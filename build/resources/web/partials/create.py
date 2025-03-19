from typing import List

from build.file import save_string
from . import giscus, metadata, doi, use_for, not_use_for, related_resources,\
    glossary_offcanvas, glossary_offcanvas_include, how_to_use, why_use, \
    ready_to_start, faqs, summary, item_pages, author_bios, development
from build.guideline.glossary import add_glossary_to_string, wrap_string_with_span

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

class Page:
    def __init__(self, guideline, filename, partials: List[Partial], add_glossary: bool = True):
        self.guideline = guideline
        self.partials = partials
        self.filename = filename
        self.add_glossary = add_glossary # type: ignore
    
    def create_web(self):
        string = self.create_string()
        string = self.add_glossary_to_string(string)
        save_string(string, self.filename)

    def create_string(self):
        strings = self.get_partial_strings()
        string = '\n\n'.join(strings)
        return string
        
    def get_partial_strings(self):
        for partial in self.get_partials():
            yield(partial.create_web(self.guideline))

    def get_partials(self):
        for partial in self.partials:
            if partial.required_by_guideline(self.guideline):
                yield partial
    
    def add_glossary_to_string(self, string):
        if self.add_glossary:
            string = add_glossary_to_string(string, self.guideline.glossary_dict, wrap_string_with_span)
        return string

class CopyFiles(Page):
    def create_web(self):
        string = self.create_string().strip()
        assert not string, f'Expected no string to be returned when copying a file, instead got: \n\n {string}'

def create_pages(guideline):
    partials_to_copy = [
        Partial(metadata, None),
        Partial(glossary_offcanvas, None),
        Partial(author_bios, None),
        Partial(development, None),
    ]
    copied_files = CopyFiles(guideline, None, partials_to_copy)
    pages = []
    pages.append(copied_files)
    pages.append(create_index_page(guideline))
    pages.append(Page(guideline, guideline.web_paths.faqs, [Partial(faqs, None)]))
    for item in guideline.items:
        pages.append(create_item_page(item))
        pages.append(create_giscus_page(item))
        # print('HAVE TURNED OFF GISCUS')
    return pages

def create_index_page(guideline):
    partials = [
        Partial(why_use, None),
        Partial(doi, None),
        Partial(how_to_use, None),
        Partial(use_for, None),
        Partial(not_use_for, 'has_not_use_for'),
        Partial(related_resources, 'has_related_resources'),
        Partial(summary, None),
        # Partial(item_order, None),
        # Partial(development, None),
        # Partial(how_to_cite, None),
        Partial(ready_to_start, None),
        Partial(glossary_offcanvas_include, None),
        # Partial(item_pages, 'has_open_e_and_e'),
    ]
    page = Page(
        guideline,
        guideline.destination_paths.index,
        partials,
    )
    return page

def create_item_page(item):
    item_module = item_pages.Item(item)
    partial = Partial(item_module, 'has_open_e_and_e')
    page = Page(item.guideline, item.web_path, [partial])
    return page

def create_giscus_page(item):
    item_module = giscus.Giscus(item)
    partial = Partial(item_module, 'has_open_e_and_e')
    page = Page(item.guideline, item.giscus_path, [partial])
    return page