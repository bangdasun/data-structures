def merge(lst, left, mid, right):
    """
    merge(lst, left, mid, right) -> merged list with ascend order 
    
    (1) Split lst separated by mid position
    (2) Set two pointers 
    (3) Compare the values of two pointers point at, move the smaller one 
        to the output, increase the pointer of that list by one
    (4) Repeat (3) until no values in one of the list
    (5) Move all rest elements of the list that still has values into output
    
    Time complexity O(n)
    Space complexity O(n)
    
    Could be solved recursively using linked lists 
    """
    if len(lst) < 2:
        return lst
    
    lst_left = lst[left:(mid + 1)] # since end point will be excluded
    lst_right = lst[(mid + 1):(right + 1)] 
    pointer_left, pointer_right = 0, 0
    lst_merged = [] # temp list to store the sorted elements
   
    while pointer_left < len(lst_left) and pointer_right < len(lst_right):
        if lst_left[pointer_left] > lst_right[pointer_right]:
            lst_merged.append(lst_right[pointer_right])
            pointer_right += 1
        else:
            lst_merged.append(lst_left[pointer_left])
            pointer_left += 1
    
    # append the rest list elements into temp list
    while pointer_left < len(lst_left):
        lst_merged.append(lst_left[pointer_left])
        pointer_left += 1
    
    while pointer_right < len(lst_right):
        lst_merged.append(lst_right[pointer_right])
        pointer_right += 1

    return lst_merged

# test 
lst = [2, 3, 1, 4]
print(merge(lst, 0, (len(lst) - 1) / 2, len(lst) - 1))

def mergeSort(lst, left, right):
    """
    mergeSort(lst, left, mid, right) -> sorted list with ascend order
    
    (1) Set the mid point
    (2) Sort the left part and sort the right part
    (3) Merge the sorted left part and sorted right part and return
    """
    
    if left == right:
        return lst[left:(right + 1)]
   
    mid = (left + right) / 2
    lst[left:(mid + 1)] = mergeSort(lst, left, mid)
    lst[(mid + 1):(right + 1)] = mergeSort(lst, mid + 1, right)
    return merge(lst, left, mid, right)
    

# More concise version
def merge(left, right):

    p_left, p_right = 0, 0
    lst_merged = []
    
    while p_left < len(left) and p_right < len(right):
    
        if left[p_left] < right[p_right]:
            lst_merged.append(left[p_left])
            p_left += 1
        else:
            lst_merged.append(right[p_right])
            p_right += 1
    
    while p_left < len(left):
        lst_merged.append(left[p_left])
        p_left += 1
    
    while p_right < len(right):
        lst_merged.append(right[p_right])
        p_right += 1
    
    return lst_merged

def mergeSort(lst):
    
    if len(lst) < 2:
        return lst
    
    mid = len(lst) / 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    
    return merge(left, right)
