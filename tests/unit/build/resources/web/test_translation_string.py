from unittest import TestCase

from build.resources.web.partials.translations import make_links_string, make_link 

translation = {'language':'A', 'url':'B'}

class TestTranslationString(TestCase):
    def test_make_link(self):
        self.assertEqual(make_link(translation), '[A](B)')
    
    def test_make_links_string(self):
        self.assertEqual(make_links_string([translation]), '[A](B)')
        self.assertEqual(make_links_string([translation, translation]), '[A](B) and [A](B)')
        self.assertEqual(make_links_string([translation, translation, translation]), '[A](B), [A](B), and [A](B)')

    
