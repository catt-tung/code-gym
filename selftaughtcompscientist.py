# saving my equations from studying self-taught computer scientist

# Ch4 Sorting Algorithms
# insertion sort
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i>0 and a_list[i-1] > value:
            a_list[i] = a_list[i-1]
            i = i-1
        a_list[i] = value
    return print(a_list)
insertion_sort([3, 5, 1, 7, 6, 9, 0])

# merge sort
def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind]= right_half[right_ind]
            right_ind += 1
            alist_ind += 1
    return a_list