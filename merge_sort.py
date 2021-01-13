def merge_sort(array):
    if len(array) != 1:
        left = merge_sort(array[0:(len(array) // 2)])
        right = merge_sort(array[(len(array) // 2):])

        return merge(left, right)

    return array


def merge(left, right):
    final_array = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            final_array.append(left[l])
            l += 1
        else:
            final_array.append(right[r])
            r += 1

    final_array += left[l:] + right[r:]

    return final_array
