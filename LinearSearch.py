import argparse;

parser = argparse.ArgumentParser(
                    prog='LinearSearch',
                    description='Perform a linear search for an item in a list')

#Arguments allow user to use whatever data they want in the command line

parser.add_argument('--array', '-a', nargs='+', help='Array/list to search with the algorithm')

parser.add_argument('--itemToFind','-i', type=int, help='Number you want to find in the array/list')

args = parser.parse_args()

#Below is the actual code required for the linear search
#Linear Search has Time Complexity: O(1) Best Case, O(n) Average Case, O(n) Worst Case
#Linear Search doesn't require a list to be sorted

array = args.array
item = args.itemToFind

itemFound = False

for index in range(0, len(array)): #iterate through every item in the list

    print("Currently Checking item "+array[index]+" at index ",index)
    
    if int(array[index]) == item: #compare each item to the item you want to find
        print("Your item is in the list at index: ",index)
        itemFound = True #If found tell user that it has been found and output index...
        break

if not(itemFound):
    print("Your item is not in the list") #If never found inform user

