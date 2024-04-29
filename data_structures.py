def ds_switch(case):
    while True:
        if case == 'list':
            # create
            my_list = ["0",1,2,3,4]
            print(my_list[2:7]) # Output: [2, 3, 4]

            # unpacking operator
            first, *rest = my_list
            print(rest)  # Output: [1,2,3,4]
            print(*my_list) # Output: 0 1 2 3 4 #used in function calls

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

            # unpacking operator
            first, *rest = my_tuple
            print(rest)  # Output: [2,3]
            print(*my_tuple) # Output: 1 2 3

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
        elif case == 'namedtuple': # factory function for creating tuple subclasses with named fields
            # Named tuples are particularly useful when you have data with a clear structure 
            # and want to provide semantic meaning to each element
            from collections import namedtuple

            # a namedtuple with fields 'x' and 'y'
            Point = namedtuple('Point', ['x', 'y']) # O(n)

            # instantiating 
            p1 = Point(1, 2) # O(1)
            print(p1.x, p1.y) # O(1)

            # unpacking
            x, y = p1 # O(1)

            # membership # O(n)
            print('x' in p1)  # Output: False
            print('z' in p1)  # Output: False
            print(1 in p1)  # Output: True
            print('x' in Point._fields) # Output: True
            print("2" if p1.__contains__(2) else "N/A") # Output: 2

            # replacing
            p2 = p1._replace(y=5) # O(n)
            print(p1, p2) # Output: Point(x=1, y=2) Point(x=1, y=5)

            # converting to dictionary
            p_dict = p1._asdict() # O(n)
            print(p_dict) # Output: {'x': 1, 'y': 2}

            # equality
            print(p1 == p2) # Output: False # O(n)

            # hashing
            print(hash(p1)) # Ouput: -3550055125485641917 # O(n)

            # string repr
            print(repr(p1)) # Output: Point(x=1, y=2)
            print(type(repr(p1))) # Output: <class 'str'>
            break
        elif case == 'dict':
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            my_dict = dict(a=1,b=2,c=3)

            # Accessing an item
            print(my_dict['a']) # Output: 1
            print(my_dict.get('d',0))  # Output: 0

            # Inserting / Updating an item
            my_dict['d'] = 4
            my_dict['b'] = 20
            print(my_dict) # Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4}

            # Deleting an item
            del my_dict['a'] # {'b': 20, 'c': 3, 'd': 4}

            # removing items
            my_dict.pop('b')
            print(my_dict) # {'c': 3, 'd': 4}
            my_dict['b'] = 20
            print(my_dict.popitem()) # removes the last inserted item # ('b', 20)
            print(my_dict) # {'c': 3, 'd': 4}
            
            my_dict['b'] = 20
            # Membership
            print('a' in my_dict) # Output: False


            for key, value in my_dict.items():
                print(key, value) # Output: b 20 / c 3 / d 4
            print(my_dict.keys()) # Output: dict_keys(['b', 'c', 'd'])
            print(my_dict.values()) # Output: dict_values([20, 3, 4])
            print(len(my_dict)) # Output: 3

            # copying
            copied_dict = my_dict.copy()
            print(copied_dict) # {'b': 20, 'c': 3, 'd': 4}
            copied_dict['a'] = 1
            my_dict['b'] = 2
            print(copied_dict, my_dict) # Output: {'b': 20, 'c': 3, 'd': 4, 'a': 1} {'b': 2, 'c': 3, 'd': 4}
            
            # copying mutable objects; shallow copy
            original_dict = {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}}
            copied_dict = original_dict.copy()
            copied_dict['a'].append(4)
            original_dict['a'].append(5)
            print(original_dict) # Output: {'a': [1, 2, 3, 4, 5], 'b': {'x': 10, 'y': 20}}
            print(copied_dict) # Output: {'a': [1, 2, 3, 4, 5], 'b': {'x': 10, 'y': 20}}

            original_dict.clear()

            # merging
            print(my_dict) # {'b': 2, 'c': 3, 'd': 4}
            my_dict.update(copied_dict) # if same keys exist in both dictionaries, the corresponding values in my_dict are overwritten by the values from copied_dict
            print(my_dict) # Output: {'b': {'x': 10, 'y': 20}, 'c': 3, 'd': 4, 'a': [1, 2, 3, 4, 5]}

            # merging using **
            dict1 = {'a': 1, 'b': 2}
            dict2 = {'b': 3, 'c': 4}
            merged_dict = {**dict1, **dict2} # Merge dict2 into dict1
            print(merged_dict) # Output: {'a': 1, 'b': 3, 'c': 4}
            
            # unpacking
            def unpack(c, d,**_):
                print(c,d) # Output: 3 4
            unpack(**my_dict) # Equivalent to unpack(a=[1, 2, 3, 4, 5], .., d=4)

            # creating dictionary using comprehension
            squares = {x:x*x for x in range(5)}
            print(squares) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
            
            # filter
            squares = {x[0]:x[1] for x in squares.items() if x[0]%2==0}
            print(squares) # Output: {0: 0, 2: 4, 4: 16}

            print({k for k in my_dict}) # Output: {'a', 'c', 'b', 'd'}

            # map
            my_dict = {'a': 1, 'b': 2}
            my_dict = dict(map(lambda item: (item[0], item[1]*2), my_dict.items()))
            print(my_dict) # Output: {'a': 2, 'b': 4}
            
            another_dict = {k: lambda x: x*x for k in my_dict} # {a:<ref to lambda>, b:<ref to lambda>}
            print(another_dict['a'](5)) # Output: 25

            x = ('key1', 'key2', 'key3')
            y = 0
            thisdict = dict.fromkeys(x, y) # {'key1': 0, 'key2': 0, 'key3': 0}
            thisdict = dict.fromkeys(x) # {'key1': None, 'key2': None, 'key3': None}
            x = thisdict.setdefault("key4", 0) # Output: 0

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