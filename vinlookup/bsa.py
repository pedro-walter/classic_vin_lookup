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
import os
                                    
class BsaPart():
    def __init__(self):
        self.class_ = None
        self.year = None
        self.model = None
        self.type_ = None
        self.description = None 
        
    def __repr__(self):
        return "<BsaPart:Class="+self.class_+\
                       ";Year="+str(self.year)+\
                       ";Model="+self.model+\
                       ";Type="+self.type_+\
                       ";Description="+self.description+">"
                       
    def __str__(self):
        return "{0}#, {1} {2} {3} {4}".format(
            self.type_,
            self.class_,
            self.model,
            self.description,
            self.year
        )
                       
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__
                       
 
class BsaMatcher():
    """                          
    Used for matching a BSA Part Number with it's corresponding BSA Part.
    The Part Numbers have the format: <Code>-<Range#>
    """
    def __init__(self):
        self.bsa_part = None
        self.regex = None
        self.range_start = None
        self.range_end = None               

#Parse parameters file
param_file = open(os.path.join(os.path.dirname(__file__),'bsa_params.csv'), encoding='utf-8')
bsa_matchers = []    
for line in param_file:
    if line.startswith('#'):
        continue
                                       
    columns = re.split('\t+',line)
    
    bsa_part = BsaPart()
    bsa_part.class_      = columns[0]
    bsa_part.year        = int(columns[1])
    bsa_part.model       = columns[2]
    bsa_part.type_       = columns[3]
    bsa_part.description = columns[4]
    
    bsa_matcher = BsaMatcher()
    bsa_matcher.bsa_part    = bsa_part
    bsa_matcher.regex       = columns[5]
    bsa_matcher.range_start = int(columns[6])
    bsa_matcher.range_end   = int(columns[7])
    
    bsa_matchers.append(bsa_matcher)
    
def decode(vin):
    """
    Intup is frame or engine number, see /notes/BSA_VINS.xlsx
    Ouptut is a list (in case the search is not spesific) of matching Search (match) returns:
    :param vin: frame or engine number
    :return: matching model(s), year(s) and part(s) details
    """
    vin = vin.lower()
    match_list = []
    for matcher in bsa_matchers:
        match = re.match(matcher.regex, vin)
        if match:
            try:
                vin_num = match.groups()[0]
                if matcher.range_start <= int(vin_num) <= matcher.range_end:
                    match_list.append(matcher.bsa_part)
            except:
                pass   
    return match_list
    
if __name__ == '__main__':
    #Prepare command-line execution
    import argparse
    
    parser = argparse.ArgumentParser(description='BSA number analyser')
    parser.add_argument('--number', '-n', help='BSA NUMBER to be analyzed')
    parser.add_argument('--run-tests', action='store_true', help='Run a few tests')
    
    args = parser.parse_args()
    
    if args.run_tests:
        vins = [
            'DD-7175',
            'DDB-4309',
            'BD2S-62600',
            'DD-9277',
            'DDB-9016',                                                                                                                                               
            'BD2S-66602',
            'DD-11110',
            'DDB-12180',
            'BD2S-68290',
            'DD-13126',
            'DDB-12740',
            'BD2S-71076',
            'DD-15082',
            'DDB-15844',
            'BD2S-74322',
            'DD-15795',
            'DDB-17355',
            'BD2S-77301',
            'DD-76478',
            'DDB-52757',
            'BD2S-87562',
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