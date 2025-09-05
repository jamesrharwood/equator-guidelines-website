import csv
import ast
import re
import os

from build.file import load_string

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

def load_data():
    with open(FILE, 'r') as file_:
        data = csv.DictReader(file_)
        data = list(data)
    return data

def create():
    print('Warning: Remember to import static files too, e.g. everything saved under wp-data')
    data = load_data()
    for row in data:
        if row['slug'] in slugs_to_ignore:
            continue
        fn = get_filename(row)
        dir_ = get_dir(row)
        if not os.path.exists(dir_): # type: ignore
            os.makedirs(dir_) # type: ignore
        contents = create_contents(row)
        with open(fn, 'w') as file_:
            file_.write(contents)

def get_dir(row):
    slug = row['slug']
    return f'reporting-guidelines/{slug}'
    
def get_filename(row):
    slug = row['slug']
    return f'reporting-guidelines/{slug}/index.qmd'

def replace_urls_without_domains(text):
    text = text.replace('(/wp-', '(https://www.equator-network.org/wp-')
    text = text.replace('(/library', '(https://www.equator-network.org/library')
    return text

def create_contents(row):
    data = row['scraped_data']
    data = ast.literal_eval(data)
    title = next((x for x in data if x[0]=='title'))[1]
    data = [x for x in data if x[0] != 'title']
    rows = []
    for x in data:
        label = x[0]
        label = re.sub(r'\s*\n+\s*', '**\n**', label)
        value = x[1]
        value = replace_urls_without_domains(value)
        rows.append(ROW.format(label=label, value=value))
    rows.append(ROW.format(label='Training', value=TRAINING_TEXT))
    contents = "\n\n".join(rows)
    return TEMPLATE.format(title=title, contents=contents)

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

{contents}

:::

"""

if __name__ == '__main__':
    create()