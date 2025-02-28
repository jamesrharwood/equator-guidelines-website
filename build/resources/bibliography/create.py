from pathlib import Path

TEMPLATE = """\
@incollection{{{ID}, 
    title={{{TITLE}}}, 
    url={{{URL}}}, 
    publisher={{The UK EQUATOR Centre}}, 
    author={{#TODO}},
    editor={{#TODO}},
    booktitle={{The EQUATOR Network Reporting Guideline Platform}},
    year={{2025}},
}}"""

def create(guideline):
    web = TEMPLATE.format(
        ID='Web',
        TITLE=f'The {guideline.config["acronym"]} Reporting Guideline', 
        URL=guideline.html_paths.index,
    )
    checklist = TEMPLATE.format(
        ID='Checklist',
        TITLE=f'The {guideline.config["acronym"]} Reporting Checklist', 
        URL=guideline.html_paths.checklist,
    )
    writing_guide = TEMPLATE.format(
        ID='WritingGuide',
        TITLE=f'The {guideline.config["acronym"]} Writing Guide', 
        URL=guideline.html_paths.writing_guide,
    )
    text = '\n'.join([web, checklist, writing_guide])
    path = Path(guideline.destination_paths.bibliographies, 'self.bib')
    with open(path, 'w') as file_:
        file_.write(text)
