from pathlib import Path

TEMPLATE = """\
@incollection{{{ID}, 
    title={{{TITLE}}}, 
    url={{{URL}}}, 
    publisher={{The UK EQUATOR Centre}}, 
    author={{{AUTHOR}}},
    editor={{Harwood, J. and Albury, C. and de Beyer, J. and Schlüssel, M. and Collins, G.}},    
    booktitle={{The EQUATOR Network Reporting Guideline Platform}},
    year={{2025}},
}}"""

ARTICLE_TEMPLATE = """\
@article{{{ID}, 
    title={Effect of a Postdischarge Virtual Ward on Readmission or Death for High-Risk Patients: A Randomized Clinical Trial}, 
    volume={312}, 
    ISSN={0098-7484}, 
    url={http://dx.doi.org/10.1001/jama.2014.11492}, 
    DOI={10.1001/jama.2014.11492}, 
    number={13}, 
    journal={JAMA}, 
    publisher={American Medical Association (AMA)}, 
    author={Dhalla, Irfan A. and O’Brien, Tara and Morra, Dante and Thorpe, Kevin E. and Wong, Brian M. and Mehta, Rajin and Frost, David W. and Abrams, Howard and Ko, Françoise and Van Rooyen, Patrick and Bell, Chaim M. and Gruneir, Andrea and Lewis, Geraint H. and Daub, Stacey and Anderson, Geoff M. and Hawker, Gillian A. and Rochon, Paula A. and Laupacis, Andreas}, 
    year={2014}, 
    month=oct, 
    pages={1305} }
"""

def create(guideline):
    print('Creating bibliographies')
    citation = guideline.config['articles']['development']
    authors = ' and '.join([create_author_string(auth) for auth in citation['author']])
    web = TEMPLATE.format(
        ID='Web',
        TITLE=f'The {guideline.config["acronym"]} Reporting Guideline', 
        AUTHOR=authors,
        URL=guideline.html_paths.index,
    )
    checklist = TEMPLATE.format(
        ID='Checklist',
        TITLE=f'The {guideline.config["acronym"]} Reporting Checklist', 
        AUTHOR=authors,
        URL=guideline.html_paths.checklist,
    )
    writing_guide = TEMPLATE.format(
        ID='WritingGuide',
        TITLE=f'The {guideline.config["acronym"]} Writing Guide', 
        AUTHOR=authors,
        URL=guideline.html_paths.writing_guide,
    )
    article = (
        "@article{Citation, "
        f"title={{{citation['title']}}}, "
        f"volume={{{citation['volume']}}}, " 
        f"ISSN={{{citation['ISSN']}}}, "
        f"url={{{citation['URL']}}}, "
        f"DOI={{{citation['DOI']}}}, "
        f"number={{{citation.get('issue', '')}}}, "
        f"journal={{{citation['container-title']}}}, "
        f"publisher={{{citation.get('publisher', '')}}}, "
        f"author={{{authors}}}, "
        f"year={{{citation['issued'][0]['year']}}}, "
        f"month={{{citation['issued'][0]['month']}}}, "
        f"pages={{{citation['page']}}} "
        "}"
    )
    text = '\n'.join([web, checklist, writing_guide, article])
    path = Path(guideline.destination_paths.bibliographies, 'self.bib')
    with open(path, 'w') as file_:
        file_.write(text)

def create_authors_string(authors):
    return ' and '.join([create_author_string(auth) for auth in authors])

def create_author_string(author):
    if 'literal' in author.keys():
        return author['literal']
    string = f"{author.get('non-dropping-particle', '')} {author['family']}, {author['given']}"
    string = string.strip()
    return string
