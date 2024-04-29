def builtin_switch(case):
    while True:
        if case == 'zip':
            # Zip example
            list1 = [1, 2, 3]
            list2 = ['a', 'b', 'c']
            zipped = zip(list1, list2)
            print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
            break
        elif case == 'enumerate':
            # Enumerate example
            letters = ['a', 'b', 'c']
            for index, letter in enumerate(letters):
                print(index, letter)
            break
            # Output:
            # 0 a
            # 1 b
            # 2 c
        elif case == 'range':
            # Range example
            print("Ascending")
            for i in range(0,5,1): # Output: 0 1 2 3 4
                print(i)
            print("Descending")
            for i in range(4,-1,-1):  # Output: 4 3 2 1 0
                print(i)
            break
        elif case == 'sorted':
            # Sorted example
            numbers = [3, 1, 4, 1, 5, 9, 2, 6]
            sorted_numbers = sorted(numbers)
            print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
            break
        elif case == 'sort':
            # Sort example
            numbers = [3, 1, 4, 1, 5, 9, 2, 6]
            numbers.sort()
            print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
            break
        elif case == 'abs':
            # Abs example
            print(abs(-10))  # Output: 10
            break
        elif case == 'any':
            # Any example
            bool_list = [False, False, True]
            print(any(bool_list))  # Output: True
            break
        elif case == 'all':
            # All example
            bool_list = [False, False, True]
            print(all(bool_list))  # Output: False
            break
        elif case == 'callable':
            # Callable example
            def example_func():
                print("Hello, world!")

            print(callable(example_func))  # Output: True
            break
        elif case == "id": # returns the memory address of the object which is unique but not necessarily consistent between runs
            # Id example
            x = 42
            print(id(x))  # Output: Unique identifier for x
            break
        elif case == "chr":
           # Chr example
            print(chr(65))  # Output: A
            break
        elif case == "ord":
           # Ord example
            print(ord('A'))  # Output: 65
            break
        elif case == "pow":
           # Pow example
            print(pow(2, 3))  # Output: 8
            print(2**3) 
            break
        elif case == "round":
            # Round example
            # Rounding to the nearest integer, ties to even
            print(round(3.5))  # Output: 4
            print(round(4.5))  # Output: 4

            # Rounding to a specific number of decimal places
            print(round(3.14159, 2))  # Output: 3.14
            print(round(3.14159, 3))  # Output: 3.142

            print(round(3.4))  # Output: 3
            print(round(3.6))  # Output: 4

            print(round(-3.4))  # Output: -3
            print(round(-3.6))  # Output: -4
            break
        elif case == "slice":
            # Slice example
            s = slice(2, 5)
            print("Hello, world!"[s])  # Output: llo

            my_list = [1, 2, 3, 4, 5]
            print(my_list[1:4])  # Output: [2, 3, 4]

            my_string = "Hello, World!"
            print(my_string[7:])  # Output: World!   

            my_list = [1, 2, 3, 4, 5]
            print(my_list[::2])  # Output: [1, 3, 5]    

            my_string = "Hello, World!"
            print(my_string[-6:])  # Output: World!   

            nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print(nested_list[1][0:2])  # Output: [4, 5]            
            break
        elif case =="hash": # returns a hash value used for quick comparisons and storage of objects in hash-based data structures like dictionaries and sets
            print(hash("Hello, world!"))  # Output: Unique hash value
            break
        elif case =="attr":
            class MyClass:
                y = 35

            obj = MyClass()
            setattr(obj, 'x', 42)
            print(obj.x)  # Output: 42
            print(getattr(obj, 'y'))  # Output: 35
            delattr(obj, 'x')
            print(hasattr(obj, 'x'))  # Output: False
            break
        elif case == "isinstance":
            x = 42
            print(isinstance(x, int)) # Output: True
            break
        elif case == "type":
            x = 42
            print(type(x)) # Output: <class 'int'>
            break
        elif case == "issubclass":
            class Vehicle:
                pass
            class Car(Vehicle):
                pass
            print(issubclass(Car, Vehicle))  # Output: True
            print(issubclass(Vehicle, object)) # Output: True
            break
        elif case == "eval_exec":
            # evaluates a single expression in the form of a string 
            # and returns the result
            print(eval("2 + 3"))  # Output: 5

            # executes a block of dynamically generated Python code, 
            # which can consist of multiple statements and assignments
            exec("print('Hello, world!')")  # Output: Hello, world!
            break
        elif case == "local_global":
            # Locals example
            def example_func():
                x = 42
                print(locals())

            example_func()  # Output: {'x': 42}
           
            # Globals example
            x = 42
            print(globals())  # Output: Global symbol table
            break
        elif case == "map":
            # Map example
            def square(x):
                return x ** 2

            numbers = [1, 2, 3, 4, 5]
            # map() function applies a given function to each item of an iterable
            # and returns an iterator that yields the result
            squared_numbers = list(map(square, numbers)) 
            print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
            break
        elif case == "filter":
            # Filter example
            def is_even(x):
                return x % 2 == 0
            
            numbers = [1, 2, 3, 4, 5]
            # filter() function filters elements from an iterable based on a specified function 
            # and returns an iterator that yields only the elements for which the function returns True
            even_numbers = list(filter(is_even, numbers))
            print(even_numbers)  # Output: [2, 4]
            break
        elif case == "reduce":
            from functools import reduce
            def add(x, y):
                return x + y
            
            numbers = [1, 2, 3, 4, 5]
            # reduce() function applies a rolling computation to the elements of an iterable, 
            # reducing them to a single value.
            result = reduce(add, numbers)
            print(result)  # Output: 15

            def square(acc,x):
                return acc + x ** 2
            
            # The initial value is 0, which will be passed as the first argument to the function for the first iteration
            result = reduce(square, numbers, 0)
            print(result) # Output: 55 (0 + 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 1 + 4 + 9 + 16 + 25 = 55)
            break
        elif case == "spl_symbols":
            # throwaway variable
            _, y = (3, 4)
            print(y) # Ouput: 4

            for _ in range(5):
                print("Hello!") # Output: Hello!

            # name of a module or name of a class
            print(__name__)  # Output: built_in_func

            # unpacking operators
            num = [1,2,3,4]
            first, *middle, last = num
            print(middle) #Output: [2,3]
            
            break
        else:
            print("Option does not exist")
            break