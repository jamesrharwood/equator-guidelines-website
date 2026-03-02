import sys
import re
import os

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from build.resources.web.import_from_old_website import load_data

if not os.getenv('PRODUCTION'):
    print('Skipping...Creating list of acronyms for filter...')
else:
    print('Creating list of acronyms for filter...')

    FILE = 'filters/patterns.txt'
    DATES = re.compile('\s*\d\d\d\d$')

    data = load_data()
    acronyms = ''
    for row in data:
        acronym = row['acronym'].strip()
        DATES.sub('', acronym)
        if acronym:
            acronyms += acronym
            acronyms += '\n'
    acronyms.strip()

    with open(FILE, 'w') as file_:
        file_.write(acronyms)

        