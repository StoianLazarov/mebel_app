from pprint import pprint

raz_input = {}
raz_input['width'] = 1200
raz_input['depth'] = 250
raz_input['h_raft_down'] = 320
raz_input['h_raft_up'] = 150
D_PLOSKOST = 18


def header_table():
    return '''
x\t|y\t|k_x\t|k_y\t|br\t|element
'''
def insert_table_el(elements):
    for i in elements:
        print(i)

def cal_etejerka_ali(
        width=1000,
        depth=200,
        h_raft_down=300,
        h_raft_up=100,
        **kwars):
    ''' kalculate element etejerka ali
params:
    width=1000
    depth=200,
    h_raft_down=300,
    h_raft_up=100,
    **kwars
'''


    str_x = h_raft_down + h_raft_up + (2 * D_PLOSKOST)
    str_y = depth
    kant_str_x = 1
    kant_str_y = 2

    dano_x = width - (2 * D_PLOSKOST)
    dano_y = depth
    kant_dano_x = 1
    kant_dano_y = 0
    dano_br = 2

    most_x = width - (2 * D_PLOSKOST)
    most_y = 100
    kant_most_x = 2
    kant_most_y = 0
    most_br = 1

    chelo_x = width - (2 * D_PLOSKOST)
    chelo_y = 60
    kant_chelo_x = 1
    kant_chelo_y = 0
    chelo_br = 2

    straniza = dict(
            el_x=str_x, el_y=str_y,
            k_x = kant_str_x,
            k_y=kant_str_y,
            el_br = 2)

    dano = dict(
            el_x=dano_x,
            el_y=dano_y,
            k_x=kant_dano_x,
            k_y=kant_dano_y,
            el_br=dano_br)

    most = dict(
            el_x=most_x,
            el_y=most_y,
            k_x=kant_most_x,
            k_y=kant_most_y,
            el_br=most_br)

    chelo = dict(
            el_x=chelo_x,
            el_y=chelo_y,
            k_x=kant_chelo_x,
            k_y=kant_chelo_y,
            el_br=chelo_br)

    elements = {}
    elements['strniza'] = straniza
    elements['dano'] = dano
    elements['most'] = most
    elements['chelo'] = chelo
    return elements

el = cal_etejerka_ali(**raz_input)

for i in el:
    print("{x}\t|{y}\t|{k_x}\t|{k_y}\t|{br}\t|{element}".format(
        x=el[i]['el_x'],
        y=el[i]['el_y'],
        k_x=el[i]['k_x'],
        k_y=el[i]['k_y'],
        br=el[i]['el_br'],
        element=i))

