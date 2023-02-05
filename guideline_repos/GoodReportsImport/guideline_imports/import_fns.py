import csv
import copy

from app import db
from app.models import Guideline, Item


def create_guidelines_from_csv_filepath(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as file_:
        reader = csv.DictReader(file_, restval=None)
        for row in reader:
            guideline = create_guideline_with_items_from_dict(row)
            db.session.add(guideline)
            db.session.commit()


def create_guideline_with_items_from_dict(original_data):
    data = {k: (v or None) for k, v in original_data.items() if k}
    guideline = create_guideline_from_dict(data)
    if guideline.related_to:
        parent = guideline.related_to[0]
        copy_items_from_parent_to_guideline(parent, guideline)
    return guideline


def create_guideline_from_dict(data):
    related_guideline_name = data.pop('related_to', None)
    guideline = Guideline(**data)
    if related_guideline_name:
        related_guideline = get_related(related_guideline_name)
        if related_guideline:
            guideline.add_relation(related_guideline)
    return guideline


def get_related(name):
    name = Guideline.clean_name(name)
    guideline = Guideline.query.get(name)
    return guideline


def copy_items_from_parent_to_guideline(parent, guideline):
    for item in parent.items:
        new_item = create_item_copy(item)
        guideline.items.append(new_item)


def create_item_copy(item):
    fields = ['number', 'number_EQ', 'number_display', 'sub_number',
              'text', 'text_long', 'example', 'title', 'section', 'important']
    data = {field: getattr(item, field) for field in fields}
    new_item = Item(**data)
    assert not(new_item is item)
    return new_item
