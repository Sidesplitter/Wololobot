import unittest

from src.tauntpack import TauntPack
from src.taunt import Taunt

class TauntPackTest(unittest.TestCase):

    def test_emptyName(self):

        with self.assertRaisesRegex(Exception, "Name may not be empty"):
            TauntPack("", "")

    def test_emptyDescription(self):

        with self.assertRaisesRegex(Exception, "Description may not be empty"):
            TauntPack("Test", "")

    def test_correctConstructor(self):

        tauntPack = TauntPack("Name", "Description")

        self.assertEqual("Name", tauntPack.name)
        self.assertEqual("Description", tauntPack.description)

    def test_matches(self):

        tauntPack = TauntPack("Name", "Description")

        taunt1 = Taunt("Name", "[0-9]", __file__)
        taunt2 = Taunt("Name 2", "Test", __file__)

        tauntPack.taunts.append(taunt1)
        tauntPack.taunts.append(taunt2)

        self.assertEqual(tauntPack.findMatch('1'), taunt1)
        self.assertEqual(tauntPack.findMatch('Test'), taunt2)
        self.assertEqual(tauntPack.findMatch('Nothing'), None)