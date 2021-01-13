def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for k in range(i, len(array)):
            if array[k] < array[min_index]:
                min_index = k

        array[i], array[min_index] = array[min_index], array[i]

    return array
