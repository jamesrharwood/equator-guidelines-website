import os
from flask import current_app

from app.tests.common import Base

from app.models import Guideline, Item
from app.tests.factories import ItemFactory, GuidelineFactory
from data.guideline_imports import import_fns


class TestGuidelineImport(Base):
    def test_item_copy(self):
        item = ItemFactory()
        item_copy = import_fns.create_item_copy(item)
        self.assertNotEqual(item, item_copy)
        self.assertEqual(item.text, item_copy.text)
        self.assertFalse(item is item_copy)
        new_string = 'Hello world'
        item_copy.text = new_string
        self.assertFalse(item.text == new_string)

    def test_guideline_copy(self):
        self.assertEqual(Guideline.query.count(), 0)
        filepath = os.path.join(
            current_app.config['BASEDIR'],
            'data/guideline_imports/oct_2020/guideline_import_oct_2020.csv'
        )
        import_fns.create_guidelines_from_csv_filepath(filepath)
        self.assertEqual(Guideline.query.count(), 18)

    def test_item_copy_between_guidelines(self):
        g1 = GuidelineFactory()
        self.assertEqual(g1.items.count(), 10)
        g2 = GuidelineFactory(items=[])
        self.assertEqual(g2.items.count(), 10)
        self.assertEqual(Item.query.count(), 20)
        import_fns.copy_items_from_parent_to_guideline(g1, g2)
        self.db.session.commit()
        self.assertEqual(Item.query.count(), 30)
