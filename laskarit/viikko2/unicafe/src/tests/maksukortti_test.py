import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortin_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_saldoa_vahenee_oikea_maara(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_saldo_ei_muutu_jos_liian_vahan(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_sopiva_oikea_arvo(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)

    def test_ota_rahaa_paljon_oikea_arvo(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)


