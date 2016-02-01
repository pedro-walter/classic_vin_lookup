# BSA
"""
Examples below, always return list becuase of possible multiple matches. See code for triumph.
Also see test_bsa.py
Examples:
    input:
        UYD-105
    output:
        Major Model: Bantam Sub Model: D1 Engine Start:  UYD-101 Engine # end:  Frame # start:  Frame # end:  Frame Type:  Notes and options:  Gears:  Electric: Wipac
    input:
        ZC10-112
    output:
        Major Model: C Range Sub Model: C11 Engine Start:  ZC11-101 Engine # end:  Frame # start: ZC10-101 Frame # end:  Frame Type: Rigid Notes and options:  Gears:  Electric:
"""
import re
import pdb

class BsaPart():
    def __init__(self):
        self.class_ = None
        self.year = None
        self.model = None
        self.part_type = None
        self.part_description = None 
        
    def __repr__(self):
        return "<BsaPart:Class="+self.class_+\
                       ";Year="+self.year+\
                       ";Model="+self.model+\
                       ";Type="+self.part_type+\
                       ";Description="+self.part_description+">"
 
class BsaMatcher():
    """
    Used for matching a BSA Part Number with it's corresponding BSA Part.
    The Part Numbers have the format: <Code>-<Range#>
    """
    def __init__(self):
        self.bsa_part = None
        self.regex = None
        self.range_group = None
        self.range_start = None
        self.range_end = None

#Parse parameters file
param_file = open('bsa_params.csv', encoding='utf-8')
#Ignore header
param_file.readline()
bsa_matchers = []    
while True:
    line = param_file.readline()
    if not line:
        break
                                       
    columns = re.split('\t+',line)
    
    bsa_part = BsaPart()
    bsa_part.class_           = columns[0]
    bsa_part.year             = columns[1]
    bsa_part.model            = columns[2]
    bsa_part.part_type        = columns[3]
    bsa_part.part_description = columns[4]
    
    bsa_matcher = BsaMatcher()
    bsa_matcher.bsa_part    = bsa_part
    bsa_matcher.regex       = columns[5]
    bsa_matcher.range_group = int(columns[6])
    bsa_matcher.range_start = int(columns[7])
    bsa_matcher.range_end   = int(columns[8])
    
    bsa_matchers.append(bsa_matcher)
    
def decode(vin):
    """
    Intup is frame or engine number, see /notes/BSA_VINS.xlsx
    Ouptut is a list (in case the search is not spesific) of matching Search (match) returns:
    :param vin: frame or engine number
    :return: matching model(s), year(s) and part(s) details
    """
<<<<<<< HEAD
    vin = vin.lower()
    match_list = []
    for matcher in bsa_matchers:
        match = re.match(matcher.regex, vin)
        if match:
            try:
                vin_num = match.groups()[matcher.range_group]
                if matcher.range_start <= int(vin_num) <= matcher.range_end:
                    match_list.append(matcher.bsa_part)
            except:
                pass
    return match_list
    
=======
    return pass

>>>>>>> 6fd8a2d337175f13fc23e69a7c24bcd6ecec02d5
if __name__ == '__main__':
    #Prepare command-line execution
    import argparse
    
    parser = argparse.ArgumentParser(description='BSA number analyser')
    parser.add_argument('--number', '-n', help='BSA NUMBER to be analyzed')
    parser.add_argument('--run-tests', action='store_true', help='Run a few tests')
    
    args = parser.parse_args()
    
    if args.run_tests:
        vins = [
            'UYD-105',
            'YD-105',
            'UYD-20105',
            'UYDL-105',
            'UYD-20000',
            'UYD-20001',
            'YDL-131',
            'YD1-131',
            'YD1-21034',
            'YD1S-21034',
            'YD1-42034',
            'YDL1-3560',
            'YD1S-42304',
            'YD1-63789',
            'YDL1-10000',
            'YD1-65123',
            'YD1S-67526',
            'BD2-110',
            'BD2L-120',
            'BD2S-130',
        ]
        for vin in vins:
            print("*** "+vin+" ***")
            print(decode(vin))
    elif args.number:
        #Decode given number
        print(decode(args.number))
    else:
        #Display help and info
        parser.print_help()
