class Utility:

    '''
{'count_elements': 7,
 'dano': {'br_el': 1,
          'k_long': 1,
          'k_short': 0,
          'long_el': 514,
          'short_el': 437},
 'grab': {'br_el': 1,
          'k_long': 0,
          'k_short': 0,
          'long_el': 716,
          'short_el': 548},
 'most': {'br_el': 2,
          'k_long': 0,
          'k_short': 0,
          'long_el': 514,
          'short_el': 100},
 'straniza': {'br_el': 2,
              'k_long': 1,
              'k_short': 1,
              'long_el': 787,
              'short_el': 366}}
    '''
    '''
id_elemtns  |   long (mm.)| short (mm.) |kant_long|kant_short| count (bg.)|
            |   {long_el} | {short_el}  |{k_long} |{k_short} |{br_el}     |
    '''
    @staticmethod
    def table_elements(elements):
        title = '''
id_elemtns  |   long (mm.)| short (mm.) |kant_long|kant_short| count (bg.)|
        '''
        content = '''
            |   {long_el} | {short_el}  |{k_long} |{k_short} |{br_el}     |
            '''
        print("-" * 20)
        print(title)
        content_dic = dict(elements)
        colectoin_val = content_dic.values()
        for values in colectoin_val:
            if isinstance(values, dict):
                print(content.format(
                    long_el=values["long_el"],
                    short_el=values["short_el"],
                    k_long=values["k_long"],
                    k_short=values["k_short"],
                    br_el=values["br_el"],
                    ))
        print("-" * 20)

    @staticmethod
    def set_dict(temp_x, temp_y, kant_x=0, kant_y=0, count_el=1):
        if temp_x > temp_y:
            long_el = temp_x
            long_kant = kant_x
            short_el = temp_y
            short_kant = kant_y
        else:
            long_el = temp_y
            long_kant = kant_y
            short_el = temp_x
            short_kant = kant_x
        return dict(
                long_el=long_el,
                short_el=short_el,
                k_long=long_kant,
                k_short=short_kant,
                br_el=count_el,
        )
