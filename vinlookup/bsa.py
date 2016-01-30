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


def decode(vin):
    """
    Intup is frame or engine number, see /notes/BSA_VINS.xlsx
    Ouptut is a list (in case the search is not spesific) of matching Search (match) returns:
    :param vin: frame or engine number
    :return: matching model and year details
    """
    return pass

if __name__ == '__main__':
    #Prepare command-line execution
    import argparse
    
    parser = argparse.ArgumentParser(description='BSA number analyser')
    parser.add_argument('--number', '-n', help='BSA NUMBER to be analyzed')
    parser.add_argument('--run-tests', action='store_true', help='Run a few tests')
    
    args = parser.parse_args()
    
    if args.run_tests:
        pass
        #Add tests here
    elif args.number:
        print(decode(args.number))
        #Parse number given
    else:
        #Display help and info
        parser.print_help()
