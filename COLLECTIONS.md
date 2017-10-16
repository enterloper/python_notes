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