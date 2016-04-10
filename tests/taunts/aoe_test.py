import unittest

from src.tauntpackfactory import TauntPackFactory

class AoETest(unittest.TestCase):

    tauntPack = None

    def setUp(self):

        factory = TauntPackFactory()
        self.tauntPack = factory.create('taunts/aoe')

    def tearDown(self):
        self.tauntPack = None

    def test_amount(self):
        self.assertEqual(43, len(self.tauntPack.taunts))

    def test_oh(self):

        self.assertIsNotNone(self.tauntPack.findMatch('Oh'))
        self.assertIsNotNone(self.tauntPack.findMatch('ooh'))
        self.assertIsNotNone(self.tauntPack.findMatch('ohh'))

    def test_ah(self):

        self.assertIsNotNone(self.tauntPack.findMatch('Ah'))
        self.assertIsNotNone(self.tauntPack.findMatch('aah'))
        self.assertIsNotNone(self.tauntPack.findMatch('ahh'))

