from unittest import TestCase

from build.guideline.paths import Paths

class TestPaths(TestCase):
    def test_paths(self):
        dirname = 'test'
        paths = Paths(dirname)
        self.assertTrue(paths.dir.endswith('guidelines/test'))
        self.assertTrue(paths.items_dir.endswith('guidelines/test/items'))
        self.assertTrue(paths.config.endswith('guidelines/test/config.yml'))