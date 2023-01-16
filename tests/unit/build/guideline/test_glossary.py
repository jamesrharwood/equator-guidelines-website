from unittest import TestCase

from build.guideline import glossary

class TestGlossary(TestCase):
    def test_pattern(self):
        pattern = glossary.create_pattern('hello world', 3)
        self.assertEqual(pattern, r'\b(?P<glossaryItem3>hello world)\b')
    
    def test_create_combined_pattern(self):
        glossary_dict = {'hello': 'definition1', 'world': 'definition2'}
        pattern = glossary.create_combined_pattern(glossary_dict)
        self.assertEqual(
            pattern,
            r'\b(?P<glossaryItem0>hello)\b|\b(?P<glossaryItem1>world)\b'
        )
    
    def test_match(self):
        pattern = glossary.create_regex({'a':'A', 'b':'B'})
        self.assertFalse(pattern.search('bag'))
        self.assertTrue(pattern.search('b a g'), pattern.pattern)
        self.assertTrue(pattern.search('B A G'))
    
    def test_get_match_named_group(self):
        pattern = glossary.create_regex({'hello world':'', 'hiya':''})
        match = pattern.search('Good morning hello world')
        self.assertEqual(
            'glossaryItem0',
            glossary.get_match_id(match)
        )
    
    def test_tag(self):
        tag = glossary.wrap_string_with_span('hello', 'glossary0')
        self.assertEqual(
            tag,
            '<span class="defined" data-bs-toggle="offcanvas" href="#glossary0" aria-controls="offcanvasExample" role="button">hello</span>'
        )