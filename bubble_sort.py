def bubble_sort(input_list):
    last_position = len(input_list) - 1
    made_changes = True
    while made_changes:
        made_changes = False
        for i in range(0, last_position):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                made_changes = True

        last_position -= 1

    return input_list
