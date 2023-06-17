import argparse
import math

parser = argparse.ArgumentParser(
                    prog='BinarySearch',
                    description='Perform a binary search for an item in a list')

#Arguments allow user to use whatever data they want in the command line

parser.add_argument('--array', '-a', nargs='+', help='Sorted Array/list to search with the algorithm')

parser.add_argument('--itemToFind','-i', type=int, help='Number you want to find in the array/list')

args = parser.parse_args()

#Below is the actual code required for the binary search
#Binary Search has Time Complexity: O(1) Best Case, O(log n) Average Case, O(log n) Worst Case
#Binary Search require as list to be sorted

array = args.array
item = args.itemToFind

itemFound = False

first = 0
last = len(array) - 1 #Starting boundaries of the array

while (not(itemFound) and first <= last): #Repeat until item is found or the pointers don't work anymore (item is not in list)
    
    mid = math.ceil((first + last) / 2) #find middle index in given range

    print("first: ",first,", last: ",last, ", mid: ",mid)

    print("Currently Checking item "+array[mid]+" at index ",mid)

    if int(array[mid]) < item: #item searching for is larger than middle value => Search up
        print("Item is higher than checked value, so first pointer becomes mid + 1")
        first = mid + 1
    
    elif int(array[mid]) == item: #item has been found
        itemFound = True
        print("Your item is in the list at index: ",mid)

    else: #item is lower => Search down
        print("Item is lower than checked value, so last pointer becomes mid - 1")
        last = mid - 1

    print("-------------------")


if not(itemFound):
    print("Your item is not in the list")