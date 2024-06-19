def bsearchrec(l, element, minimum, maximum):
    """Recursive approach of binary search

    Args:
        l (list): _description_
        element (int): _description_
        minimum (int): _description_
        maximum (int): _description_

    Returns:
        int: index of the searched element
    """

    if minimum == maximum:
        if l[minimum] == element:
            return minimum
        else:
            return -1
    else:
        if(minimum<=maximum):
            mid = minimum + (maximum - minimum)//2
            if l[mid] == element:
                return mid
            
            elif element > l[mid]:
                minimum = mid +1
                return bsearchrec(l, element, minimum, maximum)
            
            elif element < l[mid]:
                maximum = mid - 1
                return bsearchrec(l, element, minimum, maximum)

        

def bsearchitr(l, element):
    """Iterative Approach of binary search 

    Args:
        l (list): _description_
        element (int): _description_

    Returns:
        int: index of the searched element
    """
    minimum = 0
    maximum = len(l) -1 

    while(minimum<=maximum):
        
        mid = minimum + (maximum - minimum)//2
        # print(mid)
        if l[mid] ==  element:
            return mid
        elif element > l[mid]:
            minimum = mid + 1  
        elif element < l[mid]:
            maximum = mid - 1
    
    return -1


#driver code
if __name__ == '__main__':
    # l = [20, 45,47, 55, 67, 75, 88, 90]
    l = [6]
    minimum = 0
    maximum = len(l)-1
    element = 7
    # print(bsearchrec(l, element, minimum, maximum))

    print(bsearchitr(l, element))


