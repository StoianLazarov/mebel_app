# dolni shkafofe center front
# 01 width = 400
#   s mehanizam za dolen shkaf
# 02 width = 550
#   mivka r 500
# 03 mialna
# 04 width = 500
#   4 chekmedjeta
#       1 = 120
#       2 = 180
#       3, 4 - ostatak

def vrata(width, height, count=1):
    result = {}
    result["width"] = (width / count) - 7
    result["height"] = height - 7
    result["br"] = count
    result["kant_w"] = [result["width"], 2]
    result["kant-{}".format(result["height"])] = 2
    return result
def koruba(width, height=800, depth=500):
    result = {}
    kant = 2

    # Straniza
    str_x = depth - 40 - kant      #short
    str_y = height - 28 - 18       #long
    str_k_x = 0 # kant-short
    str_k_y = 1 # kant-lont
    str_br = 2
    result["straniza"] = [str_x, str_y, str_br, str_k_x, str_k_y]

    # Dano
    dano_x = width - (2*kant)      #width
    dano_y = depth - 40 - kant     #depth
    dano_k_x = 1     #width kant
    dano_k_y = 2     #depth kant
    dano_br = 1
    result["dano"] = [dano_x, dano_y, dano_br, dano_k_x, dano_k_y]

    # Fazer grab na shkafa
    faz_x = width
    faz_y = height
    result["fazer"] = [faz_x, faz_y, faz_br]

    # Vrata
    vrata_x = width - 40 - (kant*2)      #width
    vrata_y = height - 28 - 18 (kant*2)      #height
    vrata_k_x = 2
    vrata_k_y = 2
    vrata_br = 1
    result["wrata"] = [vrata_x, vrata_y, vrata_br, vrata_k_x, vrata_k_y]
    return result

def print_result(result:dict):
    pass

