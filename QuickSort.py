import argparse;

parser = argparse.ArgumentParser(
                    prog='Quick Sort',
                    description='Perform a Quick Sort on a list')

#Arguments allow user to use whatever data they want in the command line

parser.add_argument('--array', '-a', nargs='+', help='Array/list to sort with the algorithm')

args = parser.parse_args()

#Below is the actual code required for the Quick Sort
#Quick Sort has Time Complexity: O(nlogn) Best Case, O(nlogn) Average Case, O(n logn) Worst Case
#Quick Sort finds a 'pivot' and repeatedly decompses around the pivot before collecting values again (Merge sort speed without increased memory requirements)

Array = args.array

def partition(array, start, end):
    pivot = int(array[start]) # set pivot as your first value
    left = start + 1 #left and right become either side of remaining list
    right = end
    isComplete = False

    while not(isComplete):
        while left <= right and int(array[left]) <= pivot: #left pointer up until value it points to is > pivot
            left = left + 1
        while right >= left and int(array[right]) >= pivot:#move right pointer down until < pivot
            right = right - 1

        if right < left: #means all values must be sorted in place
            isComplete = True
        else: #switch pointer values around
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

    temp = array[start] #swap the new rightmark value with the pivot
    array[start] = array[right]
    array[right] = temp

    return right #will become the place to split values at (same array used, which values to compare just change)
        

def quicksort(array, start, end):
    if start < end:
        split = partition(array, start, end) #partition at a split point
        quicksort(array, start, split - 1) #sort each half
        quicksort(array, split + 1, end)

    return array

print("--------------------------------")
print("Sorted List:",quicksort(Array, 0, len(Array) - 1))
print("Algorithm quite complicated to explain with just output, see comments in source code")
print("--------------------------------")