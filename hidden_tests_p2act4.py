def sol_even_odd(my_list):
    ### BEGIN SOLUTION
    even = []
    odd = []
    for item in my_list:
        if item%2==0:
            even.append(item)
        else:
            odd.append(item)
    return even, odd

def input_even_odd(num_tests=20):
    from random import choices, choice
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    input_values = [[] for i in range(num_tests)]
    args = [{"my_list":[i for i in choices(options, k=choice([6, 8, 10]))]} for i in range(num_tests)]
    return input_values, args

def sol_combine_lists(list_1, list_2):
    ### BEGIN SOLUTION
    result = []
    for item1, item2 in zip(list_1, list_2):
        result.append(item1)
        result.append(item2)
    return result

def input_combine_lists(num_tests=20):
    from random import choice, choices
    args = []
    options = [i for i in range(10)]
    for i in range(num_tests):
        length = choice([3, 5, 7])
        args.append({"list_1":[choices(options, k=length)], "list_2":[choices(options, k=length)]})
    input_values = [[] for i in range(num_tests)]
    return input_values, args

def sol_find_median(my_list):
    ### BEGIN SOLUTION
    my_list.sort()
    if len(my_list)%2==1:
        middle_index = int(len(my_list)//2)
        return my_list[middle_index]
    else:
        middle_index = int(len(my_list)/2-1)
        return (my_list[middle_index]+my_list[middle_index+1])/2
    ### END SOLUTION

def input_find_median(num_tests=20):
    from random import choice, choices
    args = []
    options = [i for i in range(10)]
    for i in range(num_tests):
        args.append({"my_list":choices(options, k=choice([5, 6, 7, 8, 10]))})
    input_values = [[] for i in range(num_tests)]
    return input_values, args

def sol_find_mode(my_list):
    ### BEGIN SOLUTION
    items = []
    counts = []
    for item in my_list:
        if item in items:
            continue
        items.append(item)
        counts.append(my_list.count(item))
    max_count = max(counts)
    if counts.count(max_count) == 1:
        ind = counts.index(max_count)
        return items[ind]
    return "There is no mode"

def input_find_mode(num_tests=20):
    from random import choice, choices
    args = []
    options = [i for i in range(5)]
    for i in range(num_tests):
        args.append({"my_list":choices(options, k=choice([8, 10, 15, 3]))})
    input_values = [[] for i in range(num_tests)]
    return input_values, args

def sol_filter_list(list_1, list_2):
    ### BEGIN SOLUTION
    result = []
    for item in list_1:
        if item not in list_2:
            result.append(item)
    return result
    ### END SOLUTION

def input_filter_list(num_tests=20):
    from random import choice, choices
    args = []
    options = [i for i in range(10)]
    lengths = [4, 5, 8]
    for i in range(num_tests):
        args.append({"list_1":choices(options, k=choice(lengths)), "list_2":choices(options, k=choice(lengths))})
    input_values = [[] for i in range(num_tests)]
    return input_values, args
