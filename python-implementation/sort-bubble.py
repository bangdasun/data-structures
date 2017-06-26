def bubbleSort(lst):
    """
    bubbleSort(lst) -> sorted lst with ascend order
    
    https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
    
    (1) Swap pairs of element if the order is not satisfied
    (2) Repeat until there is no swaps needed
    
    Not suitable for large data set since the average and worst case are all O(n^2)
    
    """
    # set basic parameters
    lstsize = len(lst)
    sortedlst = lst[:]
    
    for o in range(lstsize - 1):
        swapped = False
        
        for i in range(lstsize - 1):
            if sortedlst[i] > sortedlst[i+1]:
                print('swap ' + str(sortedlst[i]) + ' and ' + str(sortedlst[i+1]))
                # swap two elements
                sortedlst[i+1], sortedlst[i] = sortedlst[i], sortedlst[i+1]
                swapped = True
                print('list is: ' + str(sortedlst))
                print('\n')
        
        if not swapped:
            break
        
    return sortedlst

lst = [14, 33, 27, 35, 10, 32, 1, 2, 3, 5, 9, 11]
bubbleSort(lst)
