"""
This porgram is meant to search through any json file for a certain word or number. This requires a list that is 
ordered alphabetically or in numeric order. if the word or number is found it will then report how many loops 
the algorithm took to find the requested item. If the word or number is not found then it will report that it could not find the it.
"""


# this is meant to get the nname of the file and the item to search for in that file from the user
import json
file_name = input('Enter the name of the JSON file you would like to search through: ')
words = []
list = []
search_word = input("What is the word you want to search for? ")


# this opens the requested JSON file and converts it into a list
with open(file_name) as file:
     words = json.load(file)
     list = words['array']



count = 0
done = False
first = 0
last = (len(list) -1)
halfway = (int(len(list) / 2))

#if the list is empty it will end not enter the loop.
if len(list) == 0:
    print(f'This list is empty, cannot find {search_word}.')
    done = True

# this loop is meant to divide a list in half and take the most center item and compute if the search word is greater or smaller than the
# item that it is comparing (which is referred to as "halfway". If the search_word is greater than the halfway then the search is narrowed
#  to half of the list with the larger items. If the search_word is smaller than the halfway then the search is narrowed to the smaller
# half of the list. The porcess above is repeated until the word is found or if there is no number for a halfway that we have not already used. 
while done == False:
    # the halfway is computed by adding the first and the last number in the items we have narrowed to and dividing them in 2
    halfway = int((last + first) / 2) 
    
    if  search_word < list[halfway]: 
        last = halfway - 1 # if "search_word" is below the halfway then "last" is changed to the halfway to narrow the search to the lower half
        count += 1

    elif list[halfway] < search_word:
        first = halfway + 1 # if "search_word" is above the halfway then "first" is changed to the halfway to narrow the search to the upper half
        count += 1

    else: 
        print('\nFound word')
        count += 1
        print(f'This took {count} iteration(s) to find {search_word}')
        done = True

    if first > last:
        print(f'Could not find {search_word} in list')
        done = True