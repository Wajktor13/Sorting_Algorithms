def insertion_sort(input_list):
    final_list = [input_list[0]]
    for i in range(1, len(input_list)):
        passed = False
        for f in range(len(final_list)):
            if input_list[i] < final_list[f]:
                final_list, uns_array = final_list[0:f], final_list[f:]
                final_list.append(input_list[i])
                final_list += uns_array
                passed = True
                break
        if not passed:
            final_list.append(input_list[i])

    return final_list

