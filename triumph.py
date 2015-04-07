__author__ = 'vincentdavis'
# Python 3
# based on this document
# http://www.britishspares.com/41.php

import re
from itertools import permutations
prefixes_69_80 = [m[0] + m[1] for m in permutations('abcdeghjknpx', 2)]

tri_50_62_code = ((r'^(\d{3,4})(n)$',          (0, 100, 9999),    'From 100N',        'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(\d{3,5})(na)$',         (0, 101, 15808),   '101NA, 15808NA',   'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^([3,4]\d{4,4})$',        (0, 32303, 44134), '32303, 44134',     'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^([4,5]\d{4,4})$',        (0, 44135, 56699), '44135, 56699',     'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^([5,6,7]\d{4,4})$',      (0, 56700, 70929), '56700, 70929',     'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^([7,8]\d{4,4})$',        (0, 70930, 82799), '70930, 82799 (A)', 'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(0\d{3,3})$',            (0, 100, 944),     'then 0100 - 0944 (B)', 'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(0\d{3,5})$',            (0, 945, 11115),   '0945, 011115',     'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(0[1,2]\d{4,4})$',       (0, 11116, 20075), '011116, 020075',    'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(02\d{4,4})$',           (0, 20076, 29363), '020076, 029363',    'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(0[2,3]\d{4,4})$',       (0, 29364, 30424), '029364, 030424 then', 'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(d)(\d{3,4})$',          (1, 101, 7726),    'then D101 - D7726', 'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(d)([7,8,9,1]\d{3,4})$', (1, 7727, 15788),  'D7727 - D15788',    'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(d)([1,2,3]\d{4,4})$',   (1, 15789, 30000), 'D15789 on',         'Engine No. Pre-Unit 500 & 650cc'),
                  (r'^(du)([1,2,3]\d{3,4})$',  (1, 101, 5824),    'DU101 - DU5824',    'Unit 650cc  Model year 1963'),
                  (r'^(du)([1,2,3]\d{3,4})$',  (1, 5825, 13374),  'DU5825 - DU513374', 'Unit 650cc  Model year 1964'),
                  (r'^(du)([1,2,3]\d{3,4})$',  (1, 13375, 24874), 'DU101 - DU5824',  'Unit 650cc  Model year 1965'),
                  (r'^(du)([1,2,3]\d{3,4})$',  (1, 24875, 44393), 'DU101 - DU5824',  'Unit 650cc  Model year 1966'),
                  (r'^(du)([1,2,3]\d{3,4})$',  (1, 44394, 66245), 'DU101 - DU5824',  'Unit 650cc  Model year 1967'),
                  (r'^(du)([1,2,3]\d{3,4})$',  (1, 66246, 85903), 'DU101 - DU5824',  'Unit 650cc  Model year 1968'),
                  (r'^(du)([1,2,3]\d{3,4})$',  (1, 85904, 90282), 'DU101 - DU5824',  'Unit 650cc  Model year 1969'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 101, 760),     'h101 - h760',     'Unit 350/500 Model year 1957'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 761, 5484),    'h761 - h5484',    'Unit 350/500 Model year 1958'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 5485, 11511),  'h5485 - h11511',  'Unit 350/500 Model year 1959'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 11512, 18611), 'h11512 - h18611', 'Unit 350/500 Model year 1960'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 18612, 25251), 'h18612 - h25251', 'Unit 350/500 Model year 1961'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 25252, 29732), 'h25252 - h29732', 'Unit 350/500 Model year 1962'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 29733, 32464), 'h29733 - h32464', 'Unit 350/500 Model year 1963'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 32465, 35986), 'h32465 - h35986', 'Unit 350/500 Model year 1964'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 35987, 40527), 'h35987 - h40527', 'Unit 350/500 Model year 1965'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 40528, 49832), 'h40528 - h49832', 'Unit 350/500 Model year 1966'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 49833, 57082), 'h49833 - h57082', 'Unit 350/500 Model year 1967'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 57083, 65572), 'h57083 - h65572', 'Unit 350/500 Model year 1968'),
                  (r'^(h)([1,2,3]\d{3,4})$',   (1, 65573, 67331), 'h65573 - h67331', 'Unit 350/500 Model year 1969'),
                  (r'^([abcdeghjknpx]{2,2})(\d+)$', None, None, 'Triumph Twins, Triples & Singles Built 68-80'),
                  (r'^([k,e,b,][d,e][a])(\d+)$', None, None, 'Triumph Twins, Triples & Singles Built 81-83'))


# # Engine No. Unit 650cc
# tri_650_63_69_code = {'1963': (101, 5824),
#                      '1964': (5825, 13374),
#                      '1965': (13375, 24874),
#                      '1966': (24875, 44393),
#                      '1967': (44394, 66245),
#                      '1968': (66246, 85903),
#                      '1969': (85904, 90282)}

# tri_57_69_code = {'1957': (101, 760),
#                   '1958': (761, 5484),
#                   '1959': (5485, 11511),
#                   '1960': (11512, 18611),
#                   '1961': (18612, 25251),
#                   '1962': (25252, 29732),
#                   '1963': (29733, 32464),
#                   '1964': (32465, 35986),
#                   '1965': (35987, 40527),
#                   '1966': (40528, 49832),
#                   '1968': (57083, 65572),
#                   '1969': (65573, 67331)}

tri_69_83_pre_code = {'a': ('January', '78-79'),
                      'b': ('February', '79-80'),
                      'c': ('March', '68-69'),
                      'd': ('April', '69-70'),
                      'e': ('May', '70-71'),
                      'g': ('June', '71-72'),
                      'h': ('July', '72-23'),
                      'j': ('August', '73-74'),
                      'k': ('September', '74-75'),
                      'n': ('October', '75-76'),
                      'p': ('November', '76-77'),
                      'x': ('December', '77-78'),
                      'ca': (None, '80-81'),
                      'da': (None, '81-82'),
                      'ea': (None, '82-83')}



def tri_50_62_match(vin):
    vin = vin.lower()
    match_list = []
    for key in tri_50_62_code:
        m1 = re.match(tri_50_62_code[key][0], vin)
        if m1:
            vin_num = m1.groups()[tri_50_62_code[key][1][0]]
            if tri_50_62_code[key][1][1] <= int(vin_num) <= tri_50_62_code[key][1][2]:
                #print(key, v)
                match_list.append(key)
    return match_list

# def tri_650_63_69(vin):
#     vin = vin.lower()
#     alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
#     g = alpha_digit.groups()
#     if g[0]=='du' and int(g[1]) >= 101 and int(g[1]) <= 90282 and len(g[1]) == len(str(int(g[1]))):
#         for key, v in tri_650_63_69_code.items():
#             if v[0] <= int(g[1]) <= v[1]:
#                 return 'Unit 650cc Model year ' + key

# def tri_57_69(vin):
#     vin = vin.lower()
#     alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
#     g = alpha_digit.groups()
#     if g[0]=='h' and int(g[1]) >= 101 and int(g[1]) <= 90282 and len(g[1]) == len(str(int(g[1]))):
#         for key, v in tri_57_69_code.items():
#             if v[0] <= int(g[1]) <= v[1]:
#                 return 'Unit 350/500 Model year ' + key

def tri_69_80(vin):
    vin = vin.lower()
    alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
    g = alpha_digit.groups()
    prefixes = [m[0] + m[1] for m in permutations('abcdeghjknpx', 2)]
    if alpha_digit and g[0] in prefixes:
        return 'Triumph Twins, Triples & Singles Built ' + tri_69_83_pre_code[g[0][0]][0] + ' 19' + tri_69_83_pre_code[g[0][1]][1]

def tri_81_83(vin):
    '''
    KDA	1981 models	Sept 1980 - Apr 1981
    EDA	1982 models	May 1981 - Jan 1982
    BEA	1983 models	Feb 1982 - Jan 1983
    T140V AEA34393 - Last model Jan 21st, 1983
    :param vin:
    :return:
    '''
    vin = vin.lower()
    alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
    g = alpha_digit.groups()
    prefixes = [m[0] + m[1] for m in permutations('abcdeghjknpx', 2)]
    if alpha_digit and g[0][:2] in prefixes and len(g[0])==3 and g[0][-1]=='a':
        return '500/650 Unit Construction Built ' + tri_69_83_pre_code[g[0][0]][0] + ' 19' + tri_69_83_pre_code[g[0][1:]][1]


###############################################
# Quick test
definitions = [tri_650_63_69, tri_57_69, tri_69_80, tri_81_83]
vins = ['HK12345', 'AEA34393', 'h29733', 'du35987']
for v in vins:
    print('**** ' + v + ' ****')
    for d in definitions:
        print(d(v))
