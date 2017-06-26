def selectionSort(lst):
    """
    selectionSort(lst) -> sorted lst with ascend order
    
    https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm
    
    (1) Set MIN to location 0
    (2) Search the minimum element in the list, THIS IS THE MAIN POINT
    (3) Swap with value at location MIN
    (4) Increment MIN to point to next element
    (5) Repeat until list is sorted
    
    The algorithm makes sure that the element before minloc is sorted,
    the algorithm will search the MINIMUM value at unsorted part (use loop and compare one by one, it's a 'greedy idea')
    
    Not suitable for large data set since the average and worst case are all O(n^2)
    """
    # set basic parameters
    lstsize = len(lst)
    sortedlst = lst[:]
    
    for i in range(lstsize):
        # set minimum location, it will increase by 1 in each iteration, no need i += 1
        minloc = i
        
        # search for the minimum value start from minimum location
        for j in range(minloc, lstsize):
            # find the location of value that small than minimum location one by one, 
            # the left part of the minloc will all greater than lst[minloc]
            if sortedlst[minloc] > sortedlst[j]:
                minloc = j
        
        # swap the current element to the element at minimum location
        # the current element will be the minimum 
        if minloc != i:
            sortedlst[minloc], sortedlst[i] = sortedlst[i], sortedlst[minloc]
            print('swap ' + str(sortedlst[minloc]) + ' and ' + str(sortedlst[i]) + \
                  ', list is ' + str(sortedlst))
    return sortedlst

selectionSort([9, 8, 7, 6, 5, 4, 3, 2, 1])
selectionSort([40, 5, 9, 8, 7, 7, 6, 0, 1, 2, 4, 5, 23, 54, 12, 90, 8, 13])
