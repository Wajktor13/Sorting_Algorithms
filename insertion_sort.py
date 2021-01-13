def insertion_sort(array):
    final_array = [array[0]]
    for i in range(1, len(array)):
        passed = False
        for f in range(len(final_array)):
            if array[i] < final_array[f]:
                final_array, uns_array = final_array[0:f], final_array[f:]
                final_array.append(array[i])
                final_array += uns_array
                passed = True
                break
        if not passed:
            final_array.append(array[i])

    return final_array

