def binarySearch(lst, left, right, val):
    """
    binarySearch(lst, left, right, val) -> location (0-index) of val in lst
    """
    
    # notice when we meet the case like search 10 in [11, 13], lst[mid] would be 11, 
    # than right - 1 would less than left
    if left >= right:
        return 'object not found'

    mid = (left + right) / 2
    if lst[mid] == val:
        return mid 
    elif lst[mid] < val:
        left = mid + 1
    else:
        right = mid - 1

    return binarySearch(lst, left, right, val)

lst = [0, 2, 3, 5, 6, 7, 9, 11, 13]
binarySearch(lst, 0, len(lst) - 1, val = 1)
