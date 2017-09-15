def partition(lst, left, right):
    """
    partition(lst, left, right) -> location of pivot after list re-organized
    
    (1) set pivot to be the rightmost value of list
    (2) split set to be left - 1
    (3) start iteration:
          if lst[i] <= pivot, swap lst[i] and lst[split + 1] // lst[split + 1] is the min val in part that greater than pivot
          increase split 
    (4) after iteration, swap lst[split + 1] and lst[right] (pivot), pivot now is at (split + 1), return it
    """
    
    pivot = lst[right]
    split = left - 1
    for i in xrange(left, right):
        if lst[i] <= pivot:
            lst[split + 1], lst[i] = lst[i], lst[split + 1]
            split += 1
    
    lst[right], lst[split + 1] = lst[split + 1], lst[right]
    return split + 1
    

def quickSort(lst, left, right):
    """
    quickSort(lst, left, right) -> sorted list with ascend order
    
    (1) re-orgainize the list using partition()
    (2) recursively call quickSort() on part of list [left, split - 1]
    (3) recursively call quickSort() on part of list [split + 1, right]
    
    no return clause since the manipulations are in-place
    """
    
    if len(lst) <= 1:
        return lst
    
    if left < right:
        split = partition(lst, left, right)
        quickSort(lst, left, split - 1)
        quickSort(lst, split + 1, right)


lst = [1, 3, 7, 2, 6, 4, 5]
print('Before sort: {}'.format(lst))
# partition(lst, left = 0, right = 6) # expected to be 4
quickSort(lst, 0, len(lst) - 1)
print('After sort: {}'.format(lst))
