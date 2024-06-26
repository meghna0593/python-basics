def get_input():
    input_list = [3,5,4,1,6,2]
    return input_list, len(input_list)


"""
Bubble Sort (Ascending Order)
The largest element gets bubbled up each iteration; hence there will be n-1 total runs
if n is the length of numbers, there will be n-1 pairs for comparison
Best Case: [1 2 3 4 5] => Time complexity is O(n); You iterate once, see there are no swaps and get out of the loop
Worst Case: [5 4 3 2 1] => Time complexity is O(n^2)
In place space complexity O(1)
Input dependent: Gives different TC for different types of input

Reference: 
https://www.youtube.com/watch?v=Dv4qLJcxus8 
https://youtu.be/KI3xrHqfWDc?si=y_zLfVpbe5Akb7c_
"""
def bubble_sort():
    numbers, n = get_input()

    swap = False # gives a best case of O(n)
    for i in range(n-1,0,-1): # n-1 runs
        print(i)
        swap = False 
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                swap = True
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        if not swap:
            break
    print(f"Bubble sort: {numbers}")


"""
Selection Sort
First minimum at index 0, second minimum at index 1 and so on. The minimum element's index is selected every iteration
Best, Avg, Worst case: Time complexity is O(n^2)
In place space complexity O(1)

Reference:
https://youtu.be/EwjnF7rFLns?si=qdMtY4ZCY6KQmqJI
https://youtu.be/CkF9Cbtl4Zk?si=1M0gnUfWPLdSwO7Z
"""
def selection_sort():
    numbers, n = get_input()
    
    for i in range(n-1):
        minIdx = i
        for j in range(i+1,n):
            if numbers[minIdx] > numbers[j]:
                minIdx = j
        numbers[i], numbers[minIdx] = numbers[minIdx], numbers[i]
    
    print(f"Selection Sort: {numbers}")


"""
Insertion Sort
Used in a specific scenario where you have a stream of integers or where the entire list is not visible in the beginning
Can't make use of merge or quick sort in such a case
Called insertion sort because elements are inserted one by one and compared each time
Worst Case: Time complexity is O(n^2)
In place space complexity O(1)

Reference:
https://youtu.be/8mJ-OhcfpYg?si=kA_GaqYuIXdZjI_x
https://youtu.be/R_wDA-PmGE4?si=0APVJ42t-pOJ9DWM
https://youtu.be/hQEVUsflZiE?si=Lvov7kaSiA36IUHj
"""
def insertion_sort():
    numbers, n = get_input()

    for i in range(1, n):
        for j in range(i,0,-1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break
    print(numbers)


def qs_partition(arr, left, right):
    i = left
    initial_pivot = right
    j = right - 1

    while i < j:
        while i < right and arr[i] < arr[initial_pivot]: # i is looking for an element greater than pivot
            i += 1
        while j > left and arr[j] > arr[initial_pivot]: # j is looking for an element lesser than pivot
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # i==j or j>i
    arr[i], arr[initial_pivot] = arr[initial_pivot], arr[i]

    return i # the actual pivot

def quick_sort_helper(arr, left, right):
    if left < right:
        pivot = qs_partition(arr, left, right)
        quick_sort_helper(arr, left, pivot - 1)
        quick_sort_helper(arr, pivot + 1, right)

"""
Quick Sort
Choose a pivot element
All elements before a pivot element are smaller, all elements after a pivot element are larger. 
Pivot element is always at the right place

Divide and Conquer strategy: divides a problem into sub-problems and solves those sub-problems 
Worst Case: O(n^2)
Best and Avg case: O(nlogn)
Quick Sort is an in-place sorting algorithm. Hence, the space complexity is O(log n) for the recursive calls made on the call stack.
However, it's important to note that Quick Sort has a worst-case space complexity of O(n) due to the recursive calls potentially 
consuming the entire stack space in scenarios where the array is partitioned in a highly unbalanced manner.

Reference:
https://www.youtube.com/watch?v=Vtckgz38QHs
https://youtu.be/9KBwdDEwal8?si=WyLnOXkggnxOPe-C

"""
def quick_sort():
    """
    Gist of how QS works:
    i is the first element
    j is the element left of the default pivot (last ele in our case)
    pivot is the last element (initially)

    i checks for a value greater than pivot
    j checks for a value lesser than pivot
    when found, swap i and j
    when i==j or j<i: swap pivot element and i element
    """
    numbers, n = get_input()
    quick_sort_helper(numbers, 0, n-1)
    print(numbers)


def merge_sort_helper(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # recursion
    merge_sort_helper(left_arr)
    merge_sort_helper(right_arr)

    # merging
    i = j = k = 0 # pointers for left_arr, right_arr and arr
    while i < len(left_arr) and j < len(right_arr): # O(min(n,m))
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # If there are any remaining elements in left_arr
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # If there are any remaining elements in right_arr
    while j < len(right_arr):
        print("j loop",arr,right_arr)
        arr[k] = right_arr[j]
        j += 1
        k += 1

"""
Merge Sort
Split list in half by divide and conquer method and evenually merge the halves after sorting them
Best, Avg and Worst Case: O(n logn)
Space Complexity: O(n) ; In each recursive call, the algorithm creates temporary arrays to store 
the divided halves of the input array. The size of these temporary arrays is proportional to the size 
of the input array.

Reference:
https://www.youtube.com/watch?v=3j0SWDX4AtU
https://youtu.be/_trEkEX_-2Q?si=GJ4SNrEivg2xoDQl
"""
def merge_sort():
    numbers, _ = get_input()
    merge_sort_helper(numbers)
    print(numbers)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def trickle_down(arr, i, upper):
    largest = i
    left_child = 2*i+1
    right_child = 2*i+2

    if left_child < upper and arr[left_child] > arr[largest]:
        largest = left_child 

    if right_child < upper and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i: # not the same element
        swap(arr, i, largest)
        trickle_down(arr, largest, upper)

def trickle_down_iterative(arr, i, upper):
    largest = i
    while True:
        left = i*2+1
        right = i*2+2

        if left < upper and arr[left] > arr[largest]:
            largest = left
        if right < upper and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            swap(arr, i, largest)
            i = largest
        else:
            break

"""
Heap Sort
First - Heapify into a max heap
Second - Remove root, replace last leaf node with root (swap root and LLN), trickle down

O(n log n): comparing n things with log n things. We trickle down by comparing elements and deciding 
which way to go
To heapify, take the last parent node
Max heap is used to sort an array in an ascending order

Last Parent = last leaf node is n-1 in a zero-indexed array, hence floor((n-1)/2)
Since the floor function rounds down to the nearest integer, floor((n-2)/2) is equivalent to ((n-1)/2)
Leaf nodes we don't have to check as they wont have child nodes to swap

Child=>  (2*parent)+1, (2*parent)+2
Parent=> floor(child/2)

Reference:
https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s (aka selection sort using the right data structure)
https://youtu.be/BzQGPA_v-vc?si=n-hR7xchbW93spSS (intro to heap)
https://youtu.be/7KhYwHfx40U?si=5jUaw0P60WUOgjbo (add / remove)
https://youtu.be/6i15PI_VP-E?si=-4DwJC16_FvaNkND (tricke up, child/parent equation)
https://youtu.be/jHZu1GV27tI?si=SKJugP1ix1L_Mv9S (trickle down)
https://youtu.be/LbB357_RwlY?si=VJ3kRYTVCn_VjKz9 (heap sort explanation)
https://youtu.be/laYrbOAmuvQ?si=ars9XzaSdBC5qOL9 (heap sort implementation)

"""
def heap_sort():
    arr, n = get_input()
    print("Before creating max heap: ",arr)

    # build a max heap
    for i in range(n // 2 - 1, -1, -1): # loop until the last parent node
        # trickle_down(arr, i, n)
        trickle_down_iterative(arr, i, n)

    print("Afer creating max heap: ",arr)

    # sorting
    # extract elements one by one, with root
    # 1. Swap root with last leaf
    # 2. trickle down / heapify
    for i in range(n - 1, 0, -1): 
        swap(arr, 0, i) # here we swap the first element with the i value because the i value will always be the greater value in that iteration
        # trickle_down(arr, 0, i) # here we heapify to get the greatest value of that iteration in idx 0
        trickle_down_iterative(arr, 0, i)
    
    print("After sorting: ",arr)
"""
Tim Sort
Insertion Sort + Merge Sort 
Divides the entire array into sub arrays of a particular size. The sub groups are called runs
The runs are sorted using insertion sort since it works best when array size is small
Merge logic of merge sort is used to merge these runs. 
Merge method performs well when the size of sub-arrays is a power of two. So the run size is usually 
picked between 32 and 64


Reference:
https://youtu.be/GhP5WbE4GYo?si=4IVNeOhcsXqWCXiD
https://youtu.be/6lkH8uvatTY?si=OPiCevSHmMKRd24h
"""
def tim_sort():
    pass


def bogo_sort():
    pass


def radix_sort():
    pass


def sorting_algo(case):
    while True:
        if case == 'bubble':
            bubble_sort()
            break
        elif case == 'selection':
            selection_sort()
            break
        elif case == 'insertion':
            insertion_sort()
            break
        elif case == 'quick':
            quick_sort()
            break
        elif case == 'merge':
            merge_sort()
            break
        elif case == 'heap':
            heap_sort()
            break
        elif case == 'tim':
            tim_sort()
            break
        elif case == 'bogo':
            bogo_sort()
            break
        elif case == 'radix':
            radix_sort()
            break
        else:
            print("Option does not exist")
            break



"""
~~ Links for algoritm explanation visually ~~
1. Bubble Sort: https://www.youtube.com/watch?v=Dv4qLJcxus8
2. Selection Sort: https://youtu.be/EwjnF7rFLns?si=qdMtY4ZCY6KQmqJI
3. Insertion Sort: https://youtu.be/8mJ-OhcfpYg?si=kA_GaqYuIXdZjI_x
4. Merge Sort: https://www.youtube.com/watch?v=3j0SWDX4AtU
5. Quick Sort: https://www.youtube.com/watch?v=Vtckgz38QHs
6. Heap Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s 
7. Tim Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
8. Counting Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
9. Radix Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
10. Bogo Sort
11. Shell Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
"""