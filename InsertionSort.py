import argparse;

parser = argparse.ArgumentParser(
                    prog='Insertion Sort',
                    description='Perform a Insertion Sort on a list')

#Arguments allow user to use whatever data they want in the command line

parser.add_argument('--array', '-a', nargs='+', help='Array/list to sort with the algorithm')

args = parser.parse_args()

#Below is the actual code required for the Insertion Sort
#Insertion Sort has Time Complexity: O(n) Best Case, O(n^2) Average Case, O(n^2) Worst Case

array = args.array

for index in range(1, len(array)): #will sort in each item in the list

    print("Sorting Item "+array[index]+" at index ",index)

    currentVal = array[index] #save initial values (they will change so variable needs to be set)
    position = index

    while position > 0 and int(array[position - 1]) > int(currentVal): #move item to sort down list until in correct position
        array[position] = array[position - 1] #move lower item up
        position = position - 1 #decrement to next position to check
    
    array[position] = currentVal #insert item into correct place
    

    print("Current State of Array: ",array)

print("List is Sorted!")