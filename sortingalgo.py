#Implement Bubble Sort:
   #- Write a Python function `bubble_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Bubble Sort algorithm.

   #- Test your implementation with sample input lists and verify the correctness of the output.

   #- Count the number of comparisons and swaps performed by Bubble Sort for each test case.

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    # Traverse through all array elements
    for i in range(n):
        # Flag to detect any swap
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            comparisons += 1
            # Traverse the array from 0 to n - i - 1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr, comparisons, swaps

# Testing the implementation with sample input lists
def test_bubble_sort():
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 0, 2, 5, -1, 4, 1],
        [],
        [1]
    ]
    
    for i, arr in enumerate(test_cases):
        sorted_arr, comparisons, swaps = bubble_sort(arr.copy())
        print(f"Test case {i + 1}: {arr}")
        print(f"Sorted array: {sorted_arr}")
        print(f"Comparisons: {comparisons}, Swaps: {swaps}")
        print("-" + "-" * 40)

# Run the tests
test_bubble_sort()


#Implement Selection Sort:
   #- Write a Python function `selection_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Selection Sort algorithm.

   #- Test your implementation with sample input lists and verify the correctness of the output.

   #- Count the number of comparisons and swaps performed by Selection Sort for each test case.

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            
    return arr, comparisons, swaps

# Testing the implementation with sample input lists
def test_selection_sort():
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 0, 2, 5, -1, 4, 1],
        [],
        [1]
    ]
    
    for i, arr in enumerate(test_cases):
        sorted_arr, comparisons, swaps = selection_sort(arr.copy())
        print(f"Test case {i + 1}: {arr}")
        print(f"Sorted array: {sorted_arr}")
        print(f"Comparisons: {comparisons}, Swaps: {swaps}")
        print("-" + "-" * 40)

# Run the tests
test_selection_sort()


# Implement Insertion Sort:
#    - Write a Python function `insertion_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Insertion Sort algorithm.

#    - Test your implementation with sample input lists and verify the correctness of the output.

#    - Count the number of comparisons and swaps performed by Insertion Sort for each test case.

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    # Traverse from 1 to n
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        
        # Only count the comparison when exiting the while loop if j >= 0
        if j >= 0:
            comparisons += 1
            
        arr[j + 1] = key
        # If we did not swap inside the while loop, count the key insertion as a swap
        if j + 1 != i:
            swaps += 1
    
    return arr, comparisons, swaps

# Testing the implementation with sample input lists
def test_insertion_sort():
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 0, 2, 5, -1, 4, 1],
        [],
        [1]
    ]
    
    for i, arr in enumerate(test_cases):
        sorted_arr, comparisons, swaps = insertion_sort(arr.copy())
        print(f"Test case {i + 1}: {arr}")
        print(f"Sorted array: {sorted_arr}")
        print(f"Comparisons: {comparisons}, Swaps: {swaps}")
        print("-" + "-" * 40)

# Run the tests
test_insertion_sort()