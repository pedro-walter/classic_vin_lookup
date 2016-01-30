from unittest import TestCase
import triumph as t


class test_tri_decode(TestCase):
    def test_years_13_23(self):
        vins = (('194878', ['Frame#, JUNIOR 2STROKE Model 1913']),
                ('7899', ['Engine#, JUNIOR 2STROKE Model 1922']))
        for v, r in vins:
            self.assertEqual(t.decode(v), r)

    def test_pre_unit_1950_1962(self):
        vins = (('du35987', ['Unit 650cc  Model year 1966']),)
        for v, r in vins:
            self.assertEqual(t.decode(v), r)

    def test_unit650(self):
        vins = (('du35987', ['Unit 650cc  Model year 1966']),)
        for v, r in vins:
            self.assertEqual(t.decode(v), r)

    def test_twin_triple(self):
        vins = (('HK12345', ['Triumph Twins, Triples & Singles Built July, 74-75 Season']),)
        for v, r in vins:
            self.assertEqual(t.decode(v), r)
