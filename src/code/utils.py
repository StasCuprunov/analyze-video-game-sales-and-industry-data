def create_empty_console_list(number_of_consoles):
    console_list = []
    for index in range(number_of_consoles):
        console_list.append(None)
    return console_list

def get_index_of_console(list_of_consoles, searched_console):
    for index in range(len(list_of_consoles)):
        if list_of_consoles[index] == searched_console:
            return index
    return -1