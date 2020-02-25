import unittest
import term_code


class TestTermCode(unittest.TestCase):

    def test_Winter_term_code(self):
        result = term_code.convert_from_term_code(2202)
        self.assertEqual("Winter 2020", result)
