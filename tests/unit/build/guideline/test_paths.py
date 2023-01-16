from unittest import TestCase

from build.paths import RepoPaths as Paths

class TestPaths(TestCase):
    def test_paths(self):
        dirname = 'test'
        paths = Paths(dirname)
        self.assertTrue(paths.dir.endswith('guideline_repos/test'))
        self.assertTrue(paths.items_dir.endswith('guideline_repos/test/items'))
        self.assertTrue(paths.config.endswith('guideline_repos/test/config.yml'))