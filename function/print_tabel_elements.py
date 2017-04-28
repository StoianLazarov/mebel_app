from pprint import pprint
result_elements = {
        'count_elements': 7,
        'dano': {
            'br_el': 1,
            'k_long': 1,
            'k_short': 0,
            'long_el': 514,
            'short_el': 437},
        'grab': {
            'br_el': 1,
            'k_long': 0,
            'k_short': 0,
            'long_el': 716,
            'short_el': 548},
        'most': {
            'br_el': 2,
            'k_long': 0,
            'k_short': 0,
            'long_el': 514,
            'short_el': 100},
        'straniza': {
            'br_el': 2,
            'k_long': 1,
            'k_short': 1,
            'long_el': 787,
            'short_el': 366}}
header_table = '''
long|short|k_long|k_short|br|detail
'''
content_table= '''
| {long_el} | {short_el} | {k_long} | {k_short} | {br_el}|
'''
# values = result_elements.values()
# count_el = 0
# for val in values:
#     if isinstance(val,dict):
#         print(content_table.format(**val))
# test_det = {'most': {
#     'br_el': 2,
#     'k_long': 0,
#     'k_short': 0,
#     'long_el': 514,
#     'short_el': 100}}
# detail = list(test_det.keys())[0]
# print(detail)
test_content_table= '''
{long_el} | {short_el} | {k_long} | {k_short} |{br_el}|\t-{detail}
'''
print(header_table)
k = result_elements.items()
for i in k:
    if isinstance(i[1], dict):
        print(test_content_table.format(
            detail=i[0],
            long_el=i[1]['long_el'],
            short_el=i[1]['short_el'],
            k_long=i[1]['k_long'],
            k_short=i[1]['k_short'],
            br_el=i[1]['br_el']))

