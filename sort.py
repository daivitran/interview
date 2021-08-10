# time complexity: O(nlogn)
# space complexity: O(n). Inplace
def merge_sort(lst):
    merge_sort_helper(lst, 0, len(lst) - 1)

def merge_sort_helper(lst, start, end):
    if end - start + 1 <= 1: # no elements, or 1 element
        return
    mid = start + (end - start) // 2
    merge_sort_helper(lst, start, mid)
    merge_sort_helper(lst, mid + 1, end)
    merge(lst, start, mid, end)

def merge(lst, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if (lst[mid] <= lst[start2]):
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):

        # If element 1 is in right place
        if (lst[start] <= lst[start2]):
            start += 1
        else:
            value = lst[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                lst[index] = lst[index - 1]
                index -= 1

            lst[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

# time complexity: O(nlogn)
# space complexity: O(logn). Inplace
def quick_sort(lst):
    pass

def radix_sort(lst):
    pass
