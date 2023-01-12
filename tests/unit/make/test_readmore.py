from unittest import TestCase 
from copy import copy

from guidelines.make.item import readmore

class TestReadmore(TestCase):
    section = readmore.Section(heading='Heading', body='text', index=0, item_index=9)
    sections = [copy(section), copy(section)]
    sections[1].index = 1

    def test_collapsible(self):
        md = readmore.create_collapsible_simple(self.section)
        self.assertTrue(md)
        self.assertTrue('.callout' in md)
        self.assertTrue('Heading' in md)
        self.assertTrue('sec-9-0' in md)
        self.assertFalse('Jump to' in md)
        self.assertFalse('Back to' in md)
    
    def test_create_body(self):
        md = readmore.create_collapsible_with_toc(self.sections)
        self.assertTrue('.callout' in md)
        self.assertTrue('Heading' in md)
        self.assertTrue('Jump to' in md)
        self.assertTrue('Back to top' in md)
        self.assertTrue('sec-9-0' in md)
        self.assertTrue('sec-9-1' in md)
    
    def test_create(self):
        self.assertEqual(
            readmore.create_collapsible([self.section]),
            readmore.create_collapsible_simple(self.section)
        )
        self.assertEqual(
            readmore.create_collapsible(self.sections),
            readmore.create_collapsible_with_toc(self.sections)
        )



