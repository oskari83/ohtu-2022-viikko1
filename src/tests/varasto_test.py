import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.varasto = Varasto(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_virheellinen_varasto(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_luo_ei_tyhjan_varaston_saldon(self):
        self.varasto = Varasto(10,5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_konstruktori_luo_negatiivisen_tyhjan_varaston_saldon(self):
        self.varasto = Varasto(10,-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_ei_tyhjan_varaston_liian_iso_saldo(self):
        self.varasto = Varasto(10,12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.varasto = Varasto(10)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_liikaa_saldoa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_lisays_lisaa_negatiivista_saldoa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_ota_negatiivista_saldoa(self):
        self.varasto = Varasto(10,2)
        self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_lisays_ota_liikaa_saldoa(self):
        self.varasto = Varasto(10,2)
        self.varasto.ota_varastosta(3)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_nimi(self):
        self.varasto = Varasto(10)
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
