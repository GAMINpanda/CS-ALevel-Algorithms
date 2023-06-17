import argparse;

parser = argparse.ArgumentParser(
                    prog='Bubble Sort',
                    description='Perform a Bubble Sort on a list')

#Arguments allow user to use whatever data they want in the command line

parser.add_argument('--array', '-a', nargs='+', help='Array/list to sort with the algorithm')

args = parser.parse_args()

#Below is the actual code required for the Bubble Sort
#Bubble sort has Time Complexity: O(n) Best Case, O(n^2) Average Case, O(n^2) Worst Case
#Iterates through the list multiple times, comparing pairs of values to swap each time

array = args.array

isSorted = False
totalIterations = 0

while not(isSorted):

    totalSwaps = 0 #Count how many swaps have been made in the cycle

    for index in range(0, len(array) - 1): #loop through entire list (-1 since checking +1 of index)

        print("Comparing "+array[index]+" and "+array[index + 1])

        if int(array[index]) > int(array[index + 1]):
            temp = array[index + 1] #Store temporarily since will be overwritted
            array[index + 1] = array[index]
            array[index] = temp #Swap values around
            totalSwaps = totalSwaps + 1

        print("Current State of Array: ",array)

    if totalSwaps == 0: #Means each value is in the correct place - List is sorted!
        isSorted = True

    totalIterations = totalIterations + 1 

print("List is sorted!")
print("Took a total of ",totalIterations," iterations")

        