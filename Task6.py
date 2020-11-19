# 6. * доп. задание Написать функцию которая уберет из dict элементы с пустыми значениями:

def remove_values(dict_to_remove):
    new_dict = {}
    for key, value in dict_to_remove.items():
        if value:
            new_dict[key] = value
    return new_dict


my_dict = {"grass": "green", "sun": "yellow", "sky": "blue", "space": "black", "destiny": None}
print(remove_values(my_dict))