def url_list_open():
    file = open("url_list.txt", "r")
    values = []

    for line in file:
        line = line.replace("\n", "")
        values.append(str(line))
    print(values)
    print(len(values))
    return values


url_list_open()
