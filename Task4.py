random_list = [1, 3, 4, 7, 8, 12, 13, 16, 20, 26, 31, 34]
def nechet_list(random_list_arg):
    new_list = []
    my_count = 0
    for i in random_list_arg:
        if i % 2 != 0:
            my_count += 1
            new_list.append(0)
        else:
            new_list.append(i)
    print(new_list, my_count)
nechet_list(random_list)
