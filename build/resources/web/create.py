import os

partials_dir = 'temp'

def create(guideline):
    qmd = create_qmd(guideline)
    with open(guideline.destination_paths.index, 'w') as file_:
        file_.write(qmd)

def create_qmd(guideline):
    includes = get_includes(guideline)
    qmd = '\n\n'.join(includes)
    return qmd
    
def get_includes(guideline):
    for path in get_partial_paths(guideline):
        yield f"{{{{< include {path} >}}}}"

def get_partial_paths(guideline):
    for partial in get_partials(guideline):
        yield os.path.join(partials_dir, partial)

def get_partials(guideline):
    for partial, requirement in partials:
        if requirement is True:
            continue
        elif getattr(guideline, requirement) is True:
            yield partial

partials = [
    ('_hero.qmd', True),
    ('_translations.qmd', 'has_translations'),
    ('_use_for.qmd', True),
    ('_not_use_for.qmd', 'has_not_use_for'),
    ('_related_resources.qmd', 'has_related_resources'),
    ('_download_resources.qmd', True),
    ('_guidance.qmd', True),
    ('_faqs.qmd', True),
    ('_training_and_support.qmd', True),
    ('_citation.qmd', True),
    ('offcanvas.html', True),
]



    

