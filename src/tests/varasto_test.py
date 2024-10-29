import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_jos_tilavuus_negatiivinen_nollataan(self):
        neg_tilavuus = Varasto(-1)

        self.assertEqual(neg_tilavuus.tilavuus, 0.0)

    def test_jos_saldo_negatiivinen_nollataan(self):
        neg_saldo = Varasto(1, -1)

        self.assertEqual(neg_saldo.saldo, 0.0)
    
    def test_lisaa_varastoon_ei_ylitä_kapasiteettia(self):
        varasto = Varasto(10, 1)
        varasto.lisaa_varastoon(20)

        self.assertEqual(varasto.saldo, 10)

    def test_lisaa_varastoon_negatiivinen_määrä_ei_muuta_saldoa(self):
        varasto = Varasto(10, 1)
        varasto.lisaa_varastoon(-5)

        self.assertEqual(varasto.saldo, 1)
    
    def test_ota_varastosta_negatiivinen_määrä_ei_muuta_saldoa(self):
        varasto = Varasto(10, 1)
        varasto.ota_varastosta(-5)

        self.assertEqual(varasto.saldo, 10)

    def test_varastosta_ei_voi_ottaa_saldoa_enempää(self):
        varasto = Varasto(10, 8)
        varasto.ota_varastosta(9)

        self.assertEqual(varasto.saldo, 0.0)

    def test__str__tulostaa_oikein(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.__str__(), "saldo = 5, vielä tilaa 5")
