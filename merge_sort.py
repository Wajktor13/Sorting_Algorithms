def merge_sort(input_list):
    if len(input_list) != 1:
        left = merge_sort(input_list[0:(len(input_list) // 2)])
        right = merge_sort(input_list[(len(input_list) // 2):])

        return merge(left, right)

    return input_list


def merge(left, right):
    final_list = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            final_list.append(left[l])
            l += 1
        else:
            final_list.append(right[r])
            r += 1

    final_list += left[l:] + right[r:]

    return final_list
