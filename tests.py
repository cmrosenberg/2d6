import twodeesix
import unittest

class TestParseArgs(unittest.TestCase):

    def test_modifiers_simple(self):

        arguments = ["2d6", "4", "+5", "-3"]

        expected = {"target": 4, "modifier": 2, "reroll": False, "dispell": False }
        actual = twodeesix.parse_args(arguments)

        self.assertDictEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
