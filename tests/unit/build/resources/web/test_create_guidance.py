import os

from unittest import TestCase
from unittest.mock import patch

from build.resources.web import create
from build.resources.web import partials
from build.resources.web.partials.create import PARTIALS
from build.guideline.guideline import Guideline
from build.paths import RepoPaths

template_dir = partials.__path__[0]  # type: ignore
template_names = [file.name for file in os.scandir(template_dir)]

CONFIG = {'doi':'123', 'id':'test'}

class TestCreateGuidance(TestCase): 
    def test_partial_requirements(self):
        keys = Guideline.__dataclass_fields__.keys()
        for partial in PARTIALS:
            if partial.required_if is None:
                continue
            requirement = partial.required_if
            self.assertTrue(requirement in keys, f"Guideline has no attr {requirement}")
    
    @patch('build.guideline.guideline.has_text')
    @patch('build.guideline.guideline.Guideline.load_items')
    @patch('build.file.open')
    def test_full_guideline(self, mock_open, mock_load_items, mock_has_text):
        gl = Guideline(
            dirname='TEST',
            config=CONFIG,
            resource_definitions={'web':[]},
            glossary_dict={},
        )
        gl.has_translations = True
        gl.has_not_use_for = True
        gl.has_related_resources = True
        gl.translations = [{'language': 'German', 'url': 'link'}]
        qmd = create.create_qmd(gl)
        for text in ['Translations', '_not_use_for', '_related_resources']:
            self.assertTrue(text in qmd, f'{text} not in qmd: \n\n{qmd}')

    @patch('build.guideline.guideline.has_text')
    @patch('build.guideline.guideline.Guideline.load_items')
    @patch('build.file.open')
    def test_empty_guideline(self, mock_open, mock_load_items, mock_has_text):
        gl = Guideline(
            dirname='TEST',
            config=CONFIG,
            resource_definitions={'web': []},
            glossary_dict={},
        )
        gl.has_translations = False
        gl.has_not_use_for = False
        gl.has_related_resources = False
        qmd = create.create_qmd(gl)
        for text in ['Translations', '_not_use_for', '_related_resources']:
            self.assertFalse(text in qmd, f'{text} should not be in qmd')

