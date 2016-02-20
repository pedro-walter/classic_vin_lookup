import os
import pprint
import re

from unittest import TestCase
try:
    from classic_vin_lookup.vinlookup import bsa
except ImportError:
    from vinlookup import bsa

class test_bsa_decode(TestCase):
    """
    These tests may not be complete or include all the results.
    """
    def _run_tests(self, filename):
        #Parse test parameters file
        filepath = os.path.join(os.path.dirname(__file__),filename)
        vins = {}
        with open(filepath, encoding='utf-8') as param_file:
            for line in param_file:
                if line.startswith('#'):
                    continue
                columns = re.split('\t+',line.strip())

                vin = columns[0]

                part = bsa.BsaPart()
                part.class_ =      columns[1]
                part.year =    int(columns[2])
                part.model =       columns[3]
                part.type_ =       columns[4]
                part.description = columns[5]

                if not vin in vins:
                    vins[vin] = [part]
                else:
                    vins[vin].append(part)

            for vin in vins:
                results = bsa.decode(vin)

                if len(results) != len(vins[vin]):
                    print("vin="+vin)
                    print("expected=\n"+pprint.pformat(vins[vin]))
                    print("results=\n"+pprint.pformat(results))
                    raise Exception(
                        "Number of resultss different than expected. "+\
                        "Expected: {0};Results: {1}".format(
                            len(vins[vin]), len(results)))
                for expected_result in vins[vin]:
                    result_found = False
                    for result in results:
                        try:
                            self.assertEqual(expected_result, result)
                            result_found = True
                            results.remove(result)
                            break
                        except Exception as e:
                            pass
                        #endtry
                    #endfor
                    if result_found == False:
                        print("vin="+vin)
                        print("expected=\n"+pprint.pformat(expected_result))
                        print("results=\n"+pprint.pformat(results))
                        raise Exception("Expected result not found.")

    def test_bantam(self):
        self._run_tests('bantam_params.csv')
    def test_crange(self):
        self._run_tests('c_class_params.csv')
    def test_brange(self):
        self._run_tests('b_range_params.csv')
    def test_brange(self):
        self._run_tests('m_range_params.csv')
    def test_brange(self):
        self._run_tests('c_range_params.csv')
    def test_brange(self):
        self._run_tests('b40_c25_b25_b44_range_params.csv')
    def test_brange(self):
        self._run_tests('a_range_params.csv')
    def test_brange(self):
        self._run_tests('scooters_params.csv')
