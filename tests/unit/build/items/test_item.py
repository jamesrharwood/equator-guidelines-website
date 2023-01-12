from unittest import TestCase 

from build.guideline.item.item import Item

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
            index = 1,
            text = text_simple
        )
        md = item.md
        self.assertFalse('Back to top' in md)
        self.assertTrue('#### 1. Title' in md)
        self.assertTrue('.grid id="id"' in md)
        self.assertTrue('sec-1-1' in md)
        self.assertFalse('sec-1-2' in md)
    
    def test_item(self):
        item = Item(
            id='id',
            title='Title',
            index=1,
            text=text
        )
        md = item.md
        self.assertTrue('Back to top' in md)
        self.assertTrue('#### 1. Title' in md)
        self.assertTrue('sec-1-1' in md, md)
        self.assertTrue('sec-1-2' in md)