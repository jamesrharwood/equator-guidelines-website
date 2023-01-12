import os

from unittest import TestCase

from build.resources.web import create, partials
from build.guideline.guideline import Guideline, Paths

template_dir = partials.__path__[0]  # type: ignore
template_names = [file.name for file in os.scandir(template_dir)]

class TestCreate(TestCase):
    def test_partial_filenames(self):
        for partial, requirement in create.partials:
            self.assertTrue(partial in template_names, f"no template named {partial}")
    
    def test_partial_requirements(self):
        keys = Guideline.__dataclass_fields__.keys()
        for partial, requirement in create.partials:
            if requirement is True:
                continue
            self.assertTrue(requirement in keys, f"Guideline has no attr {requirement}")
    
    def test_full_guideline(self):
        gl = Guideline(
            paths=Paths('test'),
            config={},
            has_translations=True,
            has_not_use_for=True,
            has_related_resources=True,
        )
        qmd = create.create(gl)
        for text in ['_translations', '_not_use_for', '_related_resources']:
            self.assertTrue(text in qmd)

    def test_empty_guideline(self):
        gl = Guideline(
            paths=Paths('test'),
            config={},
            has_translations=False,
            has_not_use_for=False,
            has_related_resources=False,
        )
        qmd = create.create(gl)
        for text in ['_translations', '_not_use_for', '_related_resources']:
            self.assertFalse(text in qmd)

