__author__ = 'vincentdavis'
# Python 3
# based on this document
# http://www.britishspares.com/41.php

import re
from itertools import permutations
prefixes_69_80 = [m[0] + m[1] for m in permutations('abcdeghjknpx', 2)]

triumph_codes = (
    (r'^(\d+)$', (0, 1, 109),         'Eng. 01 to 109 Frm. 194877 to 194883',    'Engine#, JUNIOR 2STROKE Model 1913'),
    (r'^(\d+)$', (0, 194877, 194883), 'Eng. 01 to 109 Frm. 194877 to 194883',    'Frame#, JUNIOR 2STROKE Model 1913'),
    (r'^(\d+)$', (0, 110, 790),       'Eng 110 to 790 Frm. 256191 to256876',     'Engine#, JUNIOR 2STROKE Model 1914'),
    (r'^(\d+)$', (0, 256191, 256876), 'Eng 110 to 790 Frm. 256191 to256876',     'Frame#, JUNIOR 2STROKE Model 1914'),
    (r'^(\d+)$', (0, 791, 1885),      'Eng. 791 to 1885 Frm. 256879 to 257970',  'Engine#, JUNIOR 2STROKE Model 1915'),
    (r'^(\d+)$', (0, 256879, 257970), 'Eng. 791 to 1885 Frm. 256879 to 257970',  'Frame#, JUNIOR 2STROKE Model 1915'),
    (r'^(\d+)$', (0, 1886, 2487),     'Eng. 1886 to 2487 Frm. 257971 to 258534', 'Engine#, JUNIOR 2STROKE Model 1916'),
    (r'^(\d+)$', (0, 257971, 258534), 'Eng. 1886 to 2487 Frm. 257971 to 258534', 'Frame#, JUNIOR 2STROKE Model 1916'),
    (r'^(\d+)$', (0, 2488, 2620),     'Eng. 2488 to 2620 Frm. 258535 to 258726', 'Engine#, JUNIOR 2STROKE Model 1917-18'),
    (r'^(\d+)$', (0, 258535, 258726), 'Eng. 2488 to 2620 Frm. 258535 to 258726', 'Frame#, JUNIOR 2STROKE Model 1917-18'),
    (r'^(\d+)$', (0, 2621, 3660),     'Eng. 2621 to 3660 Frm. 258727 to 259534', 'Engine#, JUNIOR 2STROKE Model 1919'),
    (r'^(\d+)$', (0, 258727, 259534), 'Eng. 2621 to 3660 Frm. 258727 to 259534', 'Frame#, JUNIOR 2STROKE Model 1919'),
    (r'^(\d+)$', (0, 3661, 5928),     'Eng. 3661 to 5928 Frm. 259535 to 600475', 'Engine#, JUNIOR 2STROKE Model 1920'),
    (r'^(\d+)$', (0, 259535, 600475), 'Eng. 3661 to 5928 Frm. 259535 to 600475', 'Frame#, JUNIOR 2STROKE Model 1920'),
    (r'^(\d+)$', (0, 5929, 7896),     'Eng. 5929 to 7896 Frm. 600476 to 603029', 'Engine#, JUNIOR 2STROKE Model 1921'),
    (r'^(\d+)$', (0, 600476, 603029), 'Eng. 5929 to 7896 Frm. 600476 to 603029', 'Frame#, JUNIOR 2STROKE Model 1921'),
    (r'^(\d+)$', (0, 7897, 8364),     'Eng. 7897 to 8364 Frm. 602562 to 603029', 'Engine#, JUNIOR 2STROKE Model 1922'),
    (r'^(\d+)$', (0, 602562, 603029), 'Eng. 7897 to 8364 Frm. 602562 to 603029', 'Frame#, JUNIOR 2STROKE Model 1922'),
    (r'^(\d+)$', (0, 8365, 8364),     'Eng. 8365 to 8364 Frm. 603030 to 651000', 'Engine#, JUNIOR 2STROKE Model 1923, 250 cc begins at 8501'),
    (r'^(\d+)$', (0, 603030, 651000), 'Eng. 8365 to 8364 Frm. 603030 to 651000', 'Frame#, JUNIOR 2STROKE Model 1923'),

    (r'^(\d{3,4})(n)$',          (0, 100, 9999),    'From 100N',        'Engine No. Pre-Unit 500 & 650cc 1950'),
    (r'^(\d{3,5})(na)$',         (0, 101, 15808),   '101NA, 15808NA',   'Engine No. Pre-Unit 500 & 650cc 1951'),
    (r'^(\d{5,5})(na)$',         (0, 101, 15808),   '15809NA, 25000NA',  'Engine No. Pre-Unit 500 & 650cc 1952'),
    (r'^([3,4]\d{4,4})$',        (0, 32303, 44134), '25000, 32302',     'Engine No. Pre-Unit 500 & 650cc 1952'),
    (r'^([3,4]\d{4,4})$',        (0, 32303, 44134), '32303, 44134',     'Engine No. Pre-Unit 500 & 650cc 1953'),
    (r'^([4,5]\d{4,4})$',        (0, 44135, 56699), '44135, 56699',     'Engine No. Pre-Unit 500 & 650cc 1954'),
    (r'^([5,6,7]\d{4,4})$',      (0, 56700, 70929), '56700, 70929',     'Engine No. Pre-Unit 500 & 650cc 1955'),
    (r'^([7,8]\d{4,4})$',        (0, 70930, 82799), '70930, 82799 (A)', 'Engine No. Pre-Unit 500 & 650cc 1956'),
    (r'^(0\d{3,3})$',            (0, 100, 944),     'then 0100 - 0944 (B)', 'Engine No. Pre-Unit 500 & 650cc 1956'),
    (r'^(0\d{3,5})$',            (0, 945, 11115),   '0945, 011115',     'Engine No. Pre-Unit 500 & 650cc 1957'),
    (r'^(0[1,2]\d{4,4})$',       (0, 11116, 20075), '011116, 020075',    'Engine No. Pre-Unit 500 & 650cc 1958'),
    (r'^(02\d{4,4})$',           (0, 20076, 29363), '020076, 029363',    'Engine No. Pre-Unit 500 & 650cc 1959'),
    (r'^(0[2,3]\d{4,4})$',       (0, 29364, 30424), '029364, 030424 then', 'Engine No. Pre-Unit 500 & 650cc 1960'),
    (r'^(d)(\d{3,4})$',          (1, 101, 7726),    'then D101 - D7726', 'Engine No. Pre-Unit 500 & 650cc 1960'),
    (r'^(d)([7,8,9,1]\d{3,4})$', (1, 7727, 15788),  'D7727 - D15788',    'Engine No. Pre-Unit 500 & 650cc 1961'),
    (r'^(d)([1,2,3]\d{4,4})$',   (1, 15789, 30000), 'D15789 on',         'Engine No. Pre-Unit 500 & 650cc 1962'),

    (r'^(du)(\d{3,4})$',         (1, 101, 5824),    'DU101 - DU5824',    'Unit 650cc  Model year 1963'),
    (r'^(du)(\d{4,5})$',         (1, 5825, 13374),  'DU5825 - DU13374', 'Unit 650cc  Model year 1964'),
    (r'^(du)(\d{5})$',           (1, 13375, 24874), 'DU13375 - DU24874',  'Unit 650cc  Model year 1965'),
    (r'^(du)(\d{5})$',           (1, 24875, 44393), 'DU24875 - DU44393',  'Unit 650cc  Model year 1966'),
    (r'^(du)(\d{5})$',           (1, 44394, 66245), 'DU44394 - DU66245',  'Unit 650cc  Model year 1967'),
    (r'^(du)(\d{5})$',           (1, 66246, 85903), 'DU66246 - DU85903',  'Unit 650cc  Model year 1968'),
    (r'^(du)(\d{5})$',           (1, 85904, 90282), 'DU85904 - DU90282',  'Unit 650cc  Model year 1969'),

    (r'^(h)(\d{3})$',     (1, 101, 760),     'h101 - h760',     'Unit 350/500 Model year 1957'),
    (r'^(h)(\d{3,4})$',   (1, 761, 5484),    'h761 - h5484',    'Unit 350/500 Model year 1958'),
    (r'^(h)(\d{4,5})$',   (1, 5485, 11511),  'h5485 - h11511',  'Unit 350/500 Model year 1959'),
    (r'^(h)(\d{5})$',     (1, 11512, 18611), 'h11512 - h18611', 'Unit 350/500 Model year 1960'),
    (r'^(h)(\d{5})$',     (1, 18612, 25251), 'h18612 - h25251', 'Unit 350/500 Model year 1961'),
    (r'^(h)(\d{5})$',     (1, 25252, 29732), 'h25252 - h29732', 'Unit 350/500 Model year 1962'),
    (r'^(h)(\d{5})$',     (1, 29733, 32464), 'h29733 - h32464', 'Unit 350/500 Model year 1963'),
    (r'^(h)(\d{5})$',     (1, 32465, 35986), 'h32465 - h35986', 'Unit 350/500 Model year 1964'),
    (r'^(h)(\d{5})$',     (1, 35987, 40527), 'h35987 - h40527', 'Unit 350/500 Model year 1965'),
    (r'^(h)(\d{5})$',     (1, 40528, 49832), 'h40528 - h49832', 'Unit 350/500 Model year 1966'),
    (r'^(h)(\d{5})$',     (1, 49833, 57082), 'h49833 - h57082', 'Unit 350/500 Model year 1967'),
    (r'^(h)(\d{5})$',     (1, 57083, 65572), 'h57083 - h65572', 'Unit 350/500 Model year 1968'),
    (r'^(h)(\d{5})$',     (1, 65573, 67331), 'h65573 - h67331', 'Unit 350/500 Model year 1969'),

    (r'^([abcdeghjknpx]{2,2})(\d+)$', None, None,   'Triumph Twins, Triples & Singles Built '),
    (r'^([k,e,b,][d,e][a])(\d+)$', None, None,      'Triumph Twins, Triples & Singles Built ')
    )

codes_69_83 = {'a': ('January', '78-79'),
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

def decode(vin):
    vin = vin.lower()
    match_list = []
    for row in triumph_codes:
        m1 = re.match(row[0], vin)
        if m1 and 'Twins' not in row[3]:
            try:
                vin_num = m1.groups()[row[1][0]]
                #print(vin_num)
                if row[1][1] <= int(vin_num) <= row[1][2]:
                    print(row[3], v)
                    match_list.append(row[3])
            except:
                pass
                
        elif m1 and 'Twins' in row[3]:
            try:
                month = codes_69_83[m1.groups()[0][0]][0]
                year = codes_69_83[m1.groups()[0][1]][1]
                print(m1.groups())
                if len(m1.groups()[0])==2:
                    result = row[3] + month + ', ' + year + ' Season'
                    match_list.append(result)
                elif len(m1.groups()[0])==3:
                    month = codes_69_83[m1.groups()[0][0]][0]
                    year = codes_69_83[m1.groups()[0][1:3]][1]
                    result = row[3] + month + ', ' + year + ' Season'
                    match_list.append(result)
            except:
                pass
#         match_list.append('Match Error')
    return match_list

###############################################
# Quick test
definitions = [decode]
#vins = ['DU5826', 'DU5824']
vins = ['HK12345', 'h29733', 'du35987', '194878', 'DU5826', 'h40528', '5928'  ]
for v in vins:
    print('**** ' + v + ' ****')
    for d in definitions:
        print(d(v))
