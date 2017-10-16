# COLLECTIONS

##LISTS (and strings)
* _Lists are collections of things that are in order._
* _Strings are similar to lists in that their individual characters are indexed._
* Strings are immutable.
* Lists are mutable, which means they can be changed in place
* Lists have an order, something comes first, second, etc
* List items can be accessed by their index using bracket notation[]
* You can make a list with [] literals or by using the list() function
* .append(value) - Add a new value onto the end of a list.
* .extend(iterable) - Make a list longer by adding on the members of another iterable.
* .insert(index, value) - Add a value to a list at a particular index.
* You can, of course, also add lists together with the + operator. To do this in place, you'd use the increment operator +=.
* del - A keyword for removing items from iterables or deleting whole variables.
* .remove() - A list method that removes items from a list by their value.
* .pop() will remove and return the last item from a list.
* .pop(index) will remove whatever item is at index, assuming something is.
* If there's nothing left in the list, or the provided index isn't available, .pop() will raise an IndexError.

## SLICES
* [start:stop]
* Both start and stop are optional. If you leave off start, the slice will start at the beginning of the iterable. If you leave off stop, the slice will continue until the end of the iterable.
* By using this behavior, you can quickly make copies of iterables by slicing them from front to back with [:].

####example:
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    letters[:2] -> ["A", "B"]
    letters[3:] -> ["D", "E", "F"]
    letters[:] -> THIS IS A COPY!! ['A', 'B', 'C', 'D', 'E', 'F']
    letters[3:5] -> ['D', 'E']
    
    messy_list = [2, 4, 3, 5, 1]
    clean_list = messy_list[:]
    clean_list.sort()
    print(messy_list, clean_list) -> [2, 4, 3, 5, 1] [1, 2, 3, 4, 5]
 
###SLICING WITH A STEP
[start:stop:step]

* Steps change how Python counts as it moves through the creation of a slice. 
* Positive steps, like 2, skip items from left to right. 
* Negative steps, like -1, move from right to left through the collection.
* The three parts of the slice syntax.
    * iterable[start:stop:step]

####example
    numbers = list(range(20))
    numbers -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    numbers[::2] -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    numbers[2::2] -> [2, 4, 6, 8, 10, 12, 14, 16, 18]
    "Oklahoma"[::2] -> 'Olhm'
    numbers[-2:] -> [18, 19]
    numbers[-2:-5] -> []
    numbers[-2:-5:-1] -> [18, 17, 16]
    numbers[::-1] -> [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    
    rainbow = ["red", "organge", "green", "yellow", "blue", "black", "white", "aqua", "purple", "pink"]
    del rainbow[5:8]
    rainbow -> ['red', 'organge', 'green', 'yellow', 'blue', 'purple', 'pink']
    rainbow[2:4] = ["yellow", "green"]
    rainbow -> ['red', 'organge', 'yellow', 'green', 'blue', 'purple', 'pink']
    rainbow[4:5] = "violet"
    rainbow -> ['red', 'organge', 'yellow', 'green', 'v', 'i', 'o', 'l', 'e', 't', 'purple', 'pink']
    del rainbow[5:11]
    rainbow -> ['red', 'organge', 'yellow', 'green', 'v', 'pink']
    rainbow[4:5] = ['purple']
    rainbow -> ['red', 'organge', 'yellow', 'green', 'purple', 'pink']
    rainbow[4:5] = ["blue", "indigo"]
    rainbow -> ['red', 'organge', 'yellow', 'green', 'blue', 'indigo', 'pink']
    rainbow[-2:] = "violet"
    rainbow -> ['red', 'organge', 'yellow', 'green', 'blue', 'v', 'i', 'o', 'l', 'e', 't']
    rainbow[-6:] = ["".join(rainbow[-6:])]
    rainbow -> ['red', 'organge', 'yellow', 'green', 'blue', 'violet']
    
        
    def first_4(value):
        return value[:4]
      
        
    def first_and_last_4(value):
      return value[:4] + value[-4:]
    
    
    def odds(value):
      return value[1::2]
      
    def reverse_evens(value):
      return value[::2][::-1]
      
    def sillycase(word):
      middle_point = int(len(word) / 2)
      first = word[:middle_point]
      last = word[middle_point:]
      
      return "".join([first.lower(), last.upper()])
    
    sillycase('treehouse') -> 'treeHOUSE'
      