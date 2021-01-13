def bubble_sort(array):
    last_position = len(array) - 1
    made_changes = True
    while made_changes:
        made_changes = False
        for i in range(0, last_position):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                made_changes = True

        last_position -= 1

    return array
