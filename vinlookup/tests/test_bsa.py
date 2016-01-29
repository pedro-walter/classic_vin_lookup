from unittest import TestCase
from vinlookup import bsa


class test_bsa_decode(TestCase):
    """
    These tests may not be complete or include all the results.
    """
    def test_bantam(self):
        vins = (('UYD-105',
                 ['Major Model: Bantam Sub Model: D1 Engine Start:  UYD-101 Engine # end:  Frame # start:  Frame # end:  Frame Type:  Notes and options:  Gears:  Electric: Wipac']),
                ('YD1-64001',
                 ['Major Model: Bantam Sub Model: D1 Engine Start:  YDL-8001 Engine # end:  Frame # start: YDIS-64001 Frame # end:  Frame Type: Spring Notes and options:  Gears:  Electric: Lucas']))
        for v, r in vins:
            self.assertEqual(bsa.decode(v), r)

     def test_crange(self):
            vins = (('ZC11-16011',
                     ['Major Model: C Range Sub Model: C11 Engine Start:  ZC11-16001 Engine # end:  Frame # start: ZC10S4-101 Frame # end:  Frame Type: Spring Notes and options:  Gears: Four-Speed Gearbox Electric: ']),
                    ('BC10S4-121',
                     ['Major Model: C Range Sub Model: C11 Engine Start:  BC11-101 Engine # end:  Frame # start: BC10S4-101 Frame # end:  Frame Type: Spring Notes and options:  Gears: Four-Speed Gearbox Electric: ']))
            for v, r in vins:
                self.assertEqual(bsa.decode(v), r)