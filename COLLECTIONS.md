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
      
      
##DICTIONARIES
* You can make dictionaries in two ways
    * name1 = dict([['first_name', 'Richard'], ['last_name', 'Boothe']])
    * name2 = {'first_name': 'Richard', 'last_name': 'Boothe'}
* .update() - Pass in a dictionary of keys and values to create or update in a single step.
* You can override a single key by assigning a new value to it. And you can delete a key by using del and the key's name.
* .pop(<key>) - like lists, dicts have .pop(). It'll return the key's value to you and then delete the key.
* .popitem() - similar to .pop() but instead of returning just the value, returns you a tuple (more in the next stage!) with the key and the value. Also, this doesn't take any arguments, you get a random key/value pair!
* .clear() - need to quickly empty out a dictionary? This method is your tool of choice, then.

* Unpacking a dictionary - Pulling multiple keys and their values of out of a dictionary to feed them to a function.
    * my_dict = {'name': 'Kenneth'}
    * "Hi, my name is {name}!".format(**my_dict) ---> "Hi, my name is Kenneth!"

* Packing a dictionary - Putting multiple keyword arguments into a single dictionary.
    * def packing(**kwargs):
         print(len(kwargs))
    * packing(name="Kenneth") ---> 1
    
    
* Looping over a dictionary loops over the keys in the dictionary, not the values.
    * my_dict = {'a': 1, 'b': 2, 'c': 3}
    * for key in my_dict:
         print(key)
    `a`
    `b`
    `c`

* `.keys()` - this method returns an iterable of all of the keys in a dictionary.
* `.values()` - this method returns an iterable of all of the values in the dictionary.
* `.items()` - this method is basically a combo of the above two. It returns an iterable of key/value pairs inside of tuples (more on them in the next stage!).

####Dictionary Examplegit 
    faculty = {
        'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 
        'Kenneth Love': ['Python Basics', 'Python Collections']
    }
     
    def num_teachers(teachers):
       return len(teachers)
        
        
    def num_courses(teachers):
        return len(courses(teachers))
        
        
    def courses(teachers):
        classes = []
        for name in teachers.keys():
            classes += teachers[name]
        return classes
        
    
    def most_courses(teachers):
        max_count = 0
        busiest_teacher = None
        for name in teachers.keys():
            class_amount = len(teachers[name])
            if class_amount > max_count:
                max_count = class_amount
                busiest_teacher = name
        return busiest_teacher
        
        
    def stats(teachers):
        output = []
        for name in teachers.keys():
            output.append([name, len(teachers[name])])
        return output    
        

##TUPLES
`my_tuple = (1, 2, 3)` \
my_tuple --> (1, 2, 3) \
`my_second_tuple = 1, 2, 3`\
my_second_tuple --> (1, 2, 3)\
`my_third_tuple = (5)`\
my_third_tuple --> 5 NOT A TUPLE!!! Tuples must have a comma\
`my_fourth_tuple = tuple([1, 2, 3])`\
my_fourth_tuple --> (1, 2, 3)\
* Tuple's are immutable
* You CAN change mutable object inside the tuple, just not primitives
* dir(my_tuple) will pull up all the built-in native Python methods
* `del` can can be used to delete entire tuples, but you can not use `del` to delete single values in a tuple.
 
##SETS
https://docs.python.org/3/library/stdtypes.html#set
* a collection of unique items that belong together
* each thing can only be in a set once
* sets are iterable collections
* each item is unique, and there isn't indices
* `set([1, 3, 5])` --> {1, 3, 5}
* `low_primes = {1, 3, 5, 7, 11, 13}`
* `low_primes.add(17)`
* `low_primes` --> {1, 3, 5, 7, 11, 17}
* the `update()` method can be used to combine or add to sets
* `low_primes.update({19, 23}, {2, 29})`
* `low_primes` -->{1, 2, 3, 5, 7, 11, 17, 19, 23, 29}
* `low_primes.add(15)` --> adds 15 to above
* `low_primes.remove(15)` --> removes the 15    
* just like with Dictionaries, if you try to reference something that doesn't exist in a set, a KeyError will occur.
* `low_primes.discard(100)` will remove if value exists, if not, it'll keep on keepin' on
* | or .union(*others) - all of the items from all of the sets
* & or .intersection(*others) - all of the common items between all of the sets
* - or .difference(*others) - all of the items in the first set that are not in the other sets
* ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets
    
    
    