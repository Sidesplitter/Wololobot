import unittest

from src.taunt import Taunt


class TestTaunt(unittest.TestCase):

    def test_nameEmpty(self):

        with self.assertRaisesRegex(Exception, "Name may not be empty"):
            Taunt("", "", "")

    def test_regexEmpty(self):

        with self.assertRaisesRegex(Exception, "Regex may not be empty"):
            Taunt("Name", "", "")

    def test_regexInvalid(self):

        with self.assertRaisesRegex(Exception, "Regex string is invalid"):
            Taunt("Name", "[", "")

    def test_pathInvalid(self):

        with self.assertRaisesRegex(Exception, "Soundfile path/that/does/not/exist does not exist"):
            Taunt("Name", '"test"', "path/that/does/not/exist")

    def test_correctConstructor(self):

        taunt = Taunt("Name", "[0-9]", __file__)

        self.assertEqual("Name", taunt.name)
        self.assertEqual("[0-9]", taunt.regex)
        self.assertEqual(__file__, taunt.path)

    def test_matches(self):

        taunt = Taunt("Name", "[0-9]", __file__)

        self.assertFalse(taunt.matches("a"))
        self.assertTrue(taunt.matches("1"))