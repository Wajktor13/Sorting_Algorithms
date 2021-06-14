def selection_sort(input_list):
    for i in range(len(input_list)):
        min_index = i
        for k in range(i, len(input_list)):
            if input_list[k] < input_list[min_index]:
                min_index = k

        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

    return input_list
