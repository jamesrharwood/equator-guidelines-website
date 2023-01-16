from unittest import TestCase 

from build.guideline.item.item import Item
from build.resources.web.partials.guidance.item import Item as WebItem

text_simple = (
    "Here is the body\n\n"
    "# Heading 1\n\n"
    "Paragraph\n\n"
)
text = text_simple + "# Heading 2\n\nParagraph"

class TestItem(TestCase):
    def test_item_simple(self):
        item = Item(
            id = 'id',
            title = 'Title',
            text = text_simple,
            filename='item.md',
        )
        item = WebItem(item, 1)
        md = item.create_web()
        self.assertFalse('Back to top' in md)
        self.assertTrue('#### 1. Title' in md)
        self.assertTrue('.grid id="id"' in md)
        self.assertTrue('sec-id-1' in md)
        self.assertFalse('sec-id-2' in md)
    
    def test_item(self):
        item = Item(
            id='id',
            title='Title',
            text=text,
            filename='test.md',
        )
        item = WebItem(item, 1)
        md = item.md
        self.assertTrue('Back to top' in md)
        self.assertTrue('#### 1. Title' in md)
        self.assertTrue('sec-id-1' in md, md)
        self.assertTrue('sec-id-2' in md)