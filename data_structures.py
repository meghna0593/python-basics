def ds_switch(case):
    while True:
        if case == 'list':
            # create
            my_list = ["0",1,2,3,4]
            print(my_list[2:7]) # Output: [2, 3, 4]
            my_list.append(5) # O(n)
            my_list.extend([6]) # O(k), k is the length of the iterable being extended
            my_list.pop(0) # O(n); however popping the element from the end of the list takes constant time O(1)
            print(my_list[1:]) # Output: [2, 3, 4, 5, 6]
            del my_list[2] # [1, 2, 4, 5, 6] # O(n)
            print(my_list[::-1]) # Output: [6, 5, 4, 2, 1]
            my_list.insert(0,0) # [0, 1, 2, 4, 5, 6] # O(n)
            my_list.remove(4) # [0, 1, 2, 5, 6] # O(n)
            
            print(my_list.index(5)) # Output: 3 # O(n)
            print(6 in my_list) # Output: True
            print(my_list.count(5)) # Output: 1 # O(n)

            my_list.sort() # modifies original list # O(n log n): Timsort algo - combines merge sort and insertion sort
            my_list.reverse() # modifies original list; [6, 5, 2, 1, 0] # O(n)
            sorted_list = sorted(my_list) # [0, 1, 2, 5, 6] # O(n log n): Timsort algo
            sorted_list = sorted(my_list, reverse=True) # [6, 5, 2, 1, 0]
            print(sorted_list) # Output: [6, 5, 2, 1, 0]

            my_list.append([1,2])
            shallow_copied_list = my_list.copy() # O(n)
            from copy import deepcopy
            deep_copied_list = deepcopy(my_list) # O(n)
            shallow_copied_list[-1][0] = 100
            my_list[-1][1]=101
            print(my_list, shallow_copied_list, deep_copied_list) # Output: [6, 5, 2, 1, 0, [100, 101]] [6, 5, 2, 1, 0, [100, 101]] [6, 5, 2, 1, 0, [1, 2]]

            my_list.clear() # [] # O(1) : sets the length of the list to zero,however deallocating the memory could take longer
            break
        elif case == 'array':
            import array
            my_array = array.array('i', [1, 2, 3, 4, 5])
            print(my_array[1:3]) # Output: array('i', [2, 3])
            print(my_array[2]) # Output: 3 
            my_array = array.array('u', ["1", "2", "3", "4", "5"])
            print(type(my_array[2])) # Output: <class 'str'>
            break
        elif case == 'tuple':
            my_tuple = (1, 2, 3)  # O(n)
            another_tuple = tuple([4, 5, 6])
            print(my_tuple[0]) # Output: 1  # O(1)
            print(my_tuple[1:4]) # Output: (2, 3)  # O(k), k being the size of the slice
            print(len(my_tuple)) # Output: 3 # O(1), the length of the tuple is stored internally

            # unpacking
            a, b, c = my_tuple # O(1)
            print(a, b, c) # Output: 1,2,3

            # concatenation
            concatenated_tuple = my_tuple + another_tuple # O(m + n)
            print(concatenated_tuple) # Output: (1, 2, 3, 4, 5, 6)

            # repitition
            repeated_tuple = my_tuple * 3 # O(m * n)
            print(repeated_tuple) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

            # membership
            print(2 in my_tuple)  # Output: True # O(n)
            
            print(repeated_tuple.count(2)) # Output: 3 # O(n)
            print(repeated_tuple.index(2)) # Output: 1 # O(n)

            sorted_tuple = tuple(sorted(repeated_tuple)) # O(n log n) + O(n) = O(n log n)
            print(sorted_tuple)  # Output: (1, 1, 1, 2, 2, 2, 3, 3, 3)

            break
        elif case == 'namedtuple':
            break
        elif case == 'dict':
            break
        elif case == 'ord_dict':
            break
        elif case == 'def_dict':
            break
        elif case == 'counter':
            break
        elif case == 'set':
            break
        elif case == 'deque':
            break
        elif case == 'stack':
            break
        elif case == 'priority_q':
            break
        elif case == 'heapq':
            break
        elif case == 'graph':
            break
        elif case == 'tree':
            break
        elif case == 'trie':
            break
        elif case == 'bloom_filter':
            break
        elif case == 'skip_list':
            break
        elif case == 'chain_map':
            break
        else:
            print("Option does not exist")
            break