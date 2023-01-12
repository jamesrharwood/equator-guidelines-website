import os

from unittest import TestCase

from build.guideline import guideline as gl

dir = os.path.dirname(os.path.realpath(__file__))
empty_fp = os.path.join(dir, 'empty.md')
not_empty_fp = os.path.join(dir, 'not_empty.md')
spaced_fp = os.path.join(dir, 'spaced.md')

class TestGuideline(TestCase):
    def test_has_translations(self):
        self.assertFalse(gl.has_translations({'translations': []}))
        self.assertTrue(gl.has_translations({'translations': [1]}))
    
    def test_has_text(self):
        self.assertFalse(gl.has_text(empty_fp))
        self.assertTrue(gl.has_text(not_empty_fp))
        self.assertTrue(gl.has_text(spaced_fp))