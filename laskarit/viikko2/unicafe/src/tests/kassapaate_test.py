import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alkuarvot(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_osto_riittavalla_kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_osto_vahalla_kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_osto_riittavalla_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_osto_vahalla_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_osto_riittavalla_kortilla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_osto_vahalla_kortilla(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_osto_riittavalla_kortilla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_osto_vahalla_kortilla(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_kortille(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_lataa_kortille_negatiivinen(self):
        kortti = Maksukortti(0)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(kortti, -1), None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
