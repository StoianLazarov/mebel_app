def read_file_data(file_data):
    input_list = []
    with open(file_data, "r") as f:
        for line in f:
            input_list.append(line.strip())
    return input_list

l = read_file_data("./input_data.txt")

