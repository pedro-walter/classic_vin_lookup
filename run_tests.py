import unittest
try:
    from vinlookup.tests.test_bsa import *
except ImportError:
    from classic_vin_lookup.vinlookup.tests.test_bsa import *

if __name__ == '__main__':
    unittest.main()
