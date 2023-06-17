import argparse;
import math

parser = argparse.ArgumentParser(
                    prog='Merge Sort',
                    description='Perform a Merge Sort on a list')

#Arguments allow user to use whatever data they want in the command line

parser.add_argument('--array', '-a', nargs='+', help='Array/list to sort with the algorithm')

args = parser.parse_args()

#Below is the actual code required for the Merge Sort
#Merge Sort has Time Complexity: O(nlogn) Best Case, O(nlogn) Average Case, O(nlogn) Worst Case

Array = args.array

def mergeSort(array, count):#recursive so need to define function (I added 'count' to help tracing but not necessary)
                            #equal sublist numbers are compared to eachother - higher means more decomposed
    count = count + 1

    if len(array) > 1: #'terminating condition' if you will
        mid = len(array) // 2 # find middle value of the list

        left = array[:mid]
        right = array[mid:] #split list up into halves

        left = mergeSort(left, count)
        right = mergeSort(right, count) #further split lists and assign 

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right): #while each array hasn't been compared
            if int(left[i]) < int(right[j]): #compare values in each list (already sorted so this is quickest)
                array[k] = left[i] #if left value is lower add as next value in the 'sorted' array
                i = i + 1 #move onto checking next value in left

            else:
                array[k] = right[j] #right[j] <= left[i] so add as next value in 'sorted' array
                j = j + 1 #move onto checking next value in right

            k = k + 1 #to get sorted array[k]

        while i < len(left): #check if left half has elements not merged...
            array[k] = left[i] #...add to the array
            i = i + 1
            k = k + 1

        while j < len(right): #repeat process for right elements
            array[k] = right[j]
            j = j + 1
            k = k + 1

    if count == 0: #to help tracing
        print("Sorted List: ",array)
    else:
        print("Sublist no",count,": ",array)

    return array

mergeSort(Array, -1)