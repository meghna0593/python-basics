def get_input():
    input_list = [6,5,4,3,2,1]
    return input_list, len(input_list)
"""
Bubble Sort (Ascending Order)
The largest element gets bubbled up each iteration; hence there will be n-1 total runs
if n is the length of numbers, there will be n-1 pairs for comparison
Best Case: [1 2 3 4 5] => Time complexity is O(n); You iterate once, see there are no swaps and get out of the loop
Worst Case: [5 4 3 2 1] => Time complexity is O(n^2)
In place space complexity
Input dependent: Gives different TC for different types of input

Reference: 
https://www.youtube.com/watch?v=Dv4qLJcxus8 
https://youtu.be/KI3xrHqfWDc?si=y_zLfVpbe5Akb7c_
"""
def bubble_sort():
    numbers, n = get_input()

    swap = False # gives a best case of O(n)
    for i in range(n-1,0,-1): # n-1 runs
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
In place space complexity 

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


def quick_sort():
    pass


def merge_sort():
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
6. Heap Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s (aka selection sort using the right data structure)
7. Tim Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
8. Counting Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
9. Radix Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
10. Bogo Sort
11. Shell Sort: https://www.youtube.com/watch?v=rbbTd-gkajw&t=1s
"""