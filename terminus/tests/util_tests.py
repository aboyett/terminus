from terminus.tests import unittest
from terminus.util import is_comment


class UtilTests(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_comment_detection(self):
        self.assertTrue(is_comment('# is a comment'))
        self.assertTrue(is_comment('## doubly commented'))
        self.assertTrue(is_comment('    ## spaced out'))
        self.assertFalse(is_comment('not a comment'))
