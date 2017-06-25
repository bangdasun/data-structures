def selectionSort(lst):
    """
    https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm
    
    Step 1 − Set MIN to location 0
    Step 2 − Search the minimum element in the list
    Step 3 − Swap with value at location MIN
    Step 4 − Increment MIN to point to next element
    Step 5 − Repeat until list is sorted
    
    selectionSort(lst) -> sorted lst with ascend order
    """
    # set basic parameters
    lstsize = len(lst)
    sortedlst = lst[:]
    
    for i in range(lstsize):
        # set minimum location, it will increase by 1 in each iteration, no need i += 1
        minloc = i
        
        # search for the minimum value start from minimum location
        for j in range(minloc, lstsize):
            # find the location of value that small than minimum location
            if sortedlst[minloc] > sortedlst[j]:
                minloc = j
        
        # swap the current element to the element at minimum location
        # the current element will be the minimum 
        sortedlst[minloc], sortedlst[i] = sortedlst[i], sortedlst[minloc]
    
    return sortedlst

selectionSort([9, 8, 7, 6, 5, 4, 3, 2, 1])
selectionSort([40, 5, 9, 8, 7, 7, 6, 0, 1, 2, 4, 5, 23, 54, 12, 90, 8, 13])
