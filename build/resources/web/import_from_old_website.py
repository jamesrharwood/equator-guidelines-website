import csv
import ast
import re
import os
import polars # type: ignore

from build.file import load_string

DIR = "reporting-guidelines"
FILE = "guideline_repos/data.csv"
TRAINING_TEXT = load_string('build/resources/partials/training/default.md')

slugs_to_ignore = [
    'consort',
    'strobe',
    'prisma',
    'stard',
    'care',
    'srqr',
    'improving-bioscience-research-reporting-the-arrive-guidelines-for-reporting-animal-research',
    'squire',    
]

slugs_to_adapt = {
    'improving-bioscience-research-reporting-the-arrive-guidelines-for-reporting-animal-research': 'arrive',
}

PRIORITY_FIELDS = [
    'Reporting guideline acronym',
    'Reporting guideline provided for?\n\n(i.e. exactly what the authors state in the paper)',
    'Relevant URLs\n\n(full-text if available)',
    'PubMed ID',
    'Primary guideline publication',
    'Explanation and elaboration papers',
    'Full bibliographic reference',
]
PRIORITY_FIELDS.reverse()

def load_data():
    with open(FILE, 'r') as file_:
        data = csv.DictReader(file_)
        data = list(data)
    return data

def load_data_ignoring_slugs():
    data = load_data()
    data = [row for row in data if row['slug'] not in slugs_to_ignore]
    return data

def create():
    print('Warning: Remember to import static files too, e.g. everything saved under wp-data')
    data = load_data_ignoring_slugs()

    for row in data:
        fn = get_filename(row)
        dir_ = get_dir(row)
        if not os.path.exists(dir_): # type: ignore
            os.makedirs(dir_) # type: ignore
        contents = create_contents(row)
        with open(fn, 'w') as file_:
            file_.write(contents)
        print(row)
        print('ONLY DOING ONE!')
        break

def get_dir(row):
    slug = row['slug']
    return f'{DIR}/{slug}'
    
def get_filename(row):
    slug = row['slug']
    return f'{DIR}/{slug}/index.qmd'

def replace_urls_without_domains(text):
    text = text.replace('(/wp-', '(https://www.equator-network.org/wp-')
    text = text.replace('(/library', '(https://www.equator-network.org/library')
    assert '(/' not in text, f'Imported guideline still has naked path: \n\n{text}'
    return text

def create_contents(row):
    data = row['scraped_data']
    data = ast.literal_eval(data)
    title = next((x for x in data if x[0]=='title'))[1]
    data = [x for x in data if x[0] != 'title']
    priority_data = []
    for field in PRIORITY_FIELDS:
        row = next((x for x in data if x[0]==field), None)
        if not row:
            continue
        priority_data.insert(0, data.pop(data.index(row)))
    priority_rows = [create_markdown_row(x) for x in priority_data]
    rows = [create_markdown_row(x) for x in data]
    priority_content = "\n\n".join(priority_rows)
    content = "\n\n".join(rows)
    return TEMPLATE.format(title=title, priority_content=priority_content, content=content)

def create_markdown_row(data_row):
    data_row = clean_data_row(data_row)
    row = ROW.format(label=data_row[0], value=data_row[1])
    return row 

def clean_data_row(row):
    label = clean_label(row[0])
    value = clean_value(row[1])
    return [label, value]

def clean_label(label):
    label = re.sub(r'\s*\n+\s*', '**\n**', label)
    return label

def clean_value(value):
    value = replace_urls_without_domains(value)
    return value


def create_df():
    data = load_data()
    attrs = [
        ('acronym', 'Acronym'),
        ('title', 'Title'),
        ('study_design', 'Study Design'),
        ('clinical_specialty', 'Clinical Speciality'),
        ('report_section', 'Report Section'),
        ('date_last_updated', 'Date Last Updated'),
        ('slug', 'slug'),
    ]
    title_template = '<a href="/'+DIR+'/{slug}">{title}</a>'
    data = [{attr[1]: row[attr[0]] for attr in attrs} for row in data]
    for row in data:
        priority = 1 if row['slug'] in slugs_to_ignore else 0
        row.update({'Priority': priority})
        if row['slug'] in slugs_to_adapt.keys():
            row.update({'slug': slugs_to_adapt[row['slug']]})
        row.update({'Title': title_template.format(title = row['Title'], slug = row['slug'])})
        row.pop('slug')
    df = polars.from_dicts(data)
    return df

ROW = """

::: {{.g-col-12 .g-col-md-4}}
**{label}**
:::

::: {{.g-col-12 .g-col-md-8}}
{value}
:::

"""

TEMPLATE = """\
---
title: "{title}"
---

::: {{.grid}}

{priority_content}
{content}

:::

"""

if __name__ == '__main__':
    create()
