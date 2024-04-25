def ds_switch(case):
    while True:
        if case == 'list':
            # create
            my_list = ["0",1,2,3,4]
            my_list.append(5)
            my_list.extend([6])
            my_list.pop(0)
            print(my_list[1:]) # Output: [2, 3, 4, 5, 6]
            del my_list[2] # [1, 2, 4, 5, 6]
            print(my_list[::-1]) # Output: [6, 5, 4, 2, 1]
            my_list.insert(0,0) # [0, 1, 2, 4, 5, 6]
            my_list.remove(4) # [0, 1, 2, 5, 6]
            
            print(my_list.index(5)) # Output: 3
            print(6 in my_list) # Output: True
            print(my_list.count(5)) # Output: 1

            my_list.sort() # modifies original list
            my_list.reverse() # modifies original list; [6, 5, 2, 1, 0]
            sorted_list = sorted(my_list) # [0, 1, 2, 5, 6]
            sorted_list = sorted(my_list, reverse=True) # [6, 5, 2, 1, 0]
            print(sorted_list) # Output: [6, 5, 2, 1, 0]

            my_list.append([1,2])
            shallow_copied_list = my_list.copy() 
            from copy import deepcopy
            deep_copied_list = deepcopy(my_list)
            shallow_copied_list[-1][0] = 100
            my_list[-1][1]=101
            print(my_list, shallow_copied_list, deep_copied_list) # Output: [6, 5, 2, 1, 0, [100, 101]] [6, 5, 2, 1, 0, [100, 101]] [6, 5, 2, 1, 0, [1, 2]]

            my_list.clear() # []
            break
        elif case == 'array':
            break
        elif case == 'tuple':
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