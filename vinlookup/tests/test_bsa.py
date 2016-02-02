import os
import pprint
import re

from unittest import TestCase
from vinlookup import bsa

class test_bsa_decode(TestCase):
    """
    These tests may not be complete or include all the results.
    """
    def test_bantam(self):
        #Parse test parameters file
        param_file = open(os.path.join(os.path.dirname(__file__),'bantam_params.csv'), encoding='utf-8')
        vins = {}
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
                print("expected="+pprint.pformat(vins[vin]))
                print("results="+pprint.pformat(results))                 
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
                    print("expected="+pprint.pformat(expected_result))
                    print("results="+pprint.pformat(results))              
                    raise Exception("Expected result not found.")                               

    # def test_crange(self):
        # vins = (('ZC11-16011',
                  # ['Major Model: C Range Sub Model: C11 Engine Start:  ZC11-16001 Engine # end:  Frame # start: ZC10S4-101 Frame # end:  Frame Type: Spring Notes and options:  Gears: Four-Speed Gearbox Electric: ']),
               # ('BC10S4-121',
                  # ['Major Model: C Range Sub Model: C11 Engine Start:  BC11-101 Engine # end:  Frame # start: BC10S4-101 Frame # end:  Frame Type: Spring Notes and options:  Gears: Four-Speed Gearbox Electric: ']))
        # for v, r in vins:
            # self.assertEqual(bsa.decode(v), r)