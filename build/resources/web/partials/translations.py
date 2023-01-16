from .read import file_to_str

def create_web(guideline):
    links_string = make_links_string(guideline.translations)
    text = file_to_str('_translations.qmd')
    text = text.format(links=links_string)
    return text

def make_links_string(translations:list[dict]) -> str:
    links = [make_link(translation) for translation in translations]
    if len (links)==1:
        string = links[0]
    elif len(links)==2:
        string = ' and '.join(links)
    else:
        string = ', '.join(links[:-1])
        string = ', and '.join([string, links[-1]])
    return string

def make_link(translation):
    return f"[{translation['language']}]({translation['url']})"