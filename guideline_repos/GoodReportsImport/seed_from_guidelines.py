# These are commands to copy paste

import json
import os
from app.models import Guideline
from app.models import Item
from app import db
import re
from collections import defaultdict
from oauth2client.service_account import ServiceAccountCredentials
import gspread


single_new_line = re.compile(r'(?<!\n)\n(?!\n)')

GUIDELINES_DATA_PATH = 'data/guidelines.txt'
META_DATA_PATH = 'data/meta.txt'
GUIDELINES_TO_SEED = []


def get_sheets():
    f = os.getenv("google-drive-credentials-path", "google-drive-credentials.json")
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(f, scope)
    account = gspread.authorize(credentials)
    sheet = account.open('Template matrix with examples.xlsx')
    mm = next((w for w in sheet.worksheets() if w.title == "DB"))
    meta = next((w for w in sheet.worksheets() if w.title == "DB-meta"))
    return mm, meta


def dump():
    mm, meta = get_sheets()
    meta_records = meta.get_all_records()
    guidelines = defaultdict(list)
    meta = defaultdict(dict)
    for r in mm.get_all_records():
        gl = Guideline.clean_name(r['REPORTING GUIDELINE'])
        guidelines[gl].append(r)
    for r in meta_records:
        gl = Guideline.clean_name(r['name'])
        meta[gl] = r
    with open(GUIDELINES_DATA_PATH, 'w') as f:
        json.dump(guidelines, f)
    with open(META_DATA_PATH, 'w') as f:
        json.dump(meta, f)


def double_lines(text):
    return single_new_line.sub("\n\n", text)


def seed(overwrite=False):
    with open(GUIDELINES_DATA_PATH, 'r') as f:
        guidelines = json.load(f)
    with open(META_DATA_PATH, 'r') as f:
        meta = json.load(f)
    for key, m in meta.items():
        gl = Guideline.query.get(key)
        if gl and not overwrite:
            print('Not overwriting {}'.format(m['name']))
            continue
        if not gl:
            print("Seeding {}".format(m['name']))
            gl = Guideline(key)
        gl.name = m['name']
        gl.for_ = m.get('for_', '')
        gl.for_medium = m.get('for_medium', '')
        gl.for_long = m.get('for_long', '')
        gl.link = m.get('equator link', '')
        gl.link_citation = m.get('citation link', '')
        gl.link_explanation = m.get('explanation link', '')
        gl.cite_as = m.get('citation text', '')
        gl.copyright = m.get('copyright')
        db.session.add(gl)
        db.session.commit()
        for i in guidelines.get(key, []):
            number = i['number']
            if not number:
                continue
            try:
                number = int(number)
            except Exception:
                continue
            item = gl.items.filter_by(number=number).first() or Item(key)
            item.number = number
            EQ = i['EQ_number']
            if type(EQ) in [str] and not EQ.strip():
                EQ = 0
            item.number_EQ = float(EQ)
            item.number_display = i['display_number']
            item.section = i.get('RG checklist heading 1')
            item.title = i.get('RG checklist heading 2')
            item.text = i.get('RG Checklist text', '').encode('utf-8')
            examples = [i.get("Example {}".format(x), "") for x in range(1, 7)]
            examples = [x for x in examples if x]
            example = "\n\n".join(examples).encode('utf-8')
            item.example = double_lines(example)
            item.text_long = double_lines(i.get("text_long", '').encode('utf-8'))
            db.session.add(item)
    db.session.commit()
    for key, m in meta.items():
        gl = Guideline.query.get(key)
        if not gl:
            continue
        gl.related = []
        relations = [r.strip() for r in m.get('related to', '').split(',') if r]
        relations = [Guideline.query.get(r) for r in relations]
        relations = [x for x in relations if x]
        gl.extras = []
        extras = [r.strip() for r in m.get('extra', '').split(',') if r]
        extras = [Guideline.query.get(r) for r in extras]
        extras = [x for x in extras if x]
        for r in relations:
            gl.add_relation(r)
        for e in extras:
            gl.add_extra(e)
        db.session.commit()
