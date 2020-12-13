list1 = [1,2,3,4,5,6]
sublist = []
start_index = 0
stop_index = 0
def nest_elements(list1, start_index, stop_index):
    '''
    Create a nested list within list1. Elements in [start_index, stop_index]
    will be in the nested list.

    Example:

        >>> x = [1,2,3,4,5,6]
        >>> y = nest_elements(x, 0, 4)
        >>> print(y)
        >>> [[1, 2, 3, 4, 5], 6]

    Parameters:
    ----------
    list1 : (list)
        A heterogeneous list.
    start_index : (int)
        The index of the first element that should be put into a nested list
        (inclusive).
    stop_index : (int)
        The index of the last element that should be put into a nested list
        (inclusive).

    Returns:
    ----------
    A copy of list1, with the elements from start_index to stop_index in a
    sub_list.
    '''
    list2 =[]

    for i, elem in enumerate(list1):
      
      if i >= start_index and i <= stop_index:
        sublist.append(elem)
      elif i < start_index or i > stop_index:
        list2.append(elem)
      else:
        list2.append(elem)
        
    return ([sublist] + list2)

print(nest_elements(list1,0,4))
  