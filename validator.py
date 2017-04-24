def valid_init(input_string, valid_options):
    input_string += " ({}): ".format(", ".join(valid_options))
    responce = input(input_string)
    while responce.lower() not in valid_options:
        responce = input(input_string)
    return responce
