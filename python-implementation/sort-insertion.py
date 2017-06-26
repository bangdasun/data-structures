def insertionSort(lst):
    """
    
    insertionSort(lst) -> sorted lst with ascend order
    
    https://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm
    
    (1) If it is the first element, it is already sorted. return 1;
    (2) Pick next element
    (3) Compare with all elements in the sorted sub-list
    (4) Shift all the elements in the sorted sub-list that is greater than the 
         value to be sorted
    (5) Insert the value
    (6) Repeat until list is sorted
    
    Not suitable for large data set since the average and worst case are all O(n^2)
    
    """
    # set basic parameters
    lstsize = len(lst)
    sortedlst = lst[:]
    
    for i in range(1, lstsize):
        # check the sorted part
        sortedpart = list(range(i))
        sortedpart.reverse()
        # insert the element
        for j in sortedpart:
            if sortedlst[j] > sortedlst[j+1]:
                sortedlst[j+1], sortedlst[j] = sortedlst[j], sortedlst[j+1]
    
    return sortedlst
    
lst = [14, 33, 27, 10, 35, 19, 42, 44]
insertionSort(lst)


def insertionSort2(lst):
    """
    Pseudocode from
    https://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm
    """
    holePosition = 0
    valueToInsert = 0
    lstsize = len(lst)
    sortedlst = lst[:]
    
    for i in range(lstsize):
        # set value to be inserted
        valueToInsert = sortedlst[i]
        holePosition = i
        
        # insert
        while holePosition > 0 and sortedlst[holePosition - 1] > valueToInsert:
            sortedlst[holePosition] = sortedlst[holePosition - 1]
            holePosition = holePosition - 1
        
        sortedlst[holePosition] = valueToInsert
    
    return sortedlst

insertionSort2(lst)
