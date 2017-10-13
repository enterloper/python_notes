#Python Basics
### Syntax and Style -
    Rules for how your code should look. Python does this so code 'looks' the same regardless of author.
    Blocks - sections of code that are related (they hold the same context, or scope)
    Indentation - blocks have an indentation of 4 spaces.
    variable and function names must use only lowercase and underscores (snake case)

### The Python Shell
    commands in the shell:
        python3 -> opens or enters python shell
        exit() -> exits python shell
        quit() -> also exits python shell
        ctrl-z -> also exits python shell
        help() -> opens the help module
        help(argument) -> provides information on the argument passed
            help(str)
        help(argument.sec_argument) -> provides information on properties of argument
            help(str.center)
            
    running scripts in the shell:
        python3 the_file_name.py
        
### Errors
    NameError - You tried to use a name (a variable, function, or other object) that doesn't exist.
        print(x) -> NameError: name 'x' is not defined
        
    TypeError - You tried to use a piece of data that's not the expected/right type or you tried to do something that a type of data can't do.
        5 + 'a' -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
        
    SyntaxError - You tried to use some invalid Python.
        print("Hello) -> SyntaxError: EOL while scanning string literal
     
     ZeroDivisionError
        10/0 -> ZeroDivisionError: division by Zero

    ValueError
    my_list = [1, 2, 3, 4, 5]
    my_list.remove(9) -> ValueError: list.remove(x): x not in list


# Data Types     

### Naming Things
    Creating a variable is always done the same way:
        variable_name = "variable value"
    
    And you can always delete a variable using:
        del variable_name
        
### Numbers
    The two built-in types of numbers in Python are int and float. Ints are whole numbers and floats are decimal numbers.

    Both number types support addition (+), subtraction (-), multiplication (*), division (/) and more.

    Division always results in a float, even if the result would be a whole number (e.g. 10 / 2 will give you 5.0).

    round() is a built-in function that will round a float to the nearest whole number.

    Dividing by zero will result in a ZeroDivisionError exception.

    You can create integers using the int() function. You can create floats using the float() function. Using int() on a float is not the same as using round() on one.
    
    0.1 + 0.1 + 0.1 - 0.3 -> 5.551115123125783e-17
    round(5.551115123125783e-17) -> 0
    int(5.2) -> 5
    int(5.9) -> 5
    int("5") -> 5
    float("5.8") -> 5.8
    float(5) -> 5.0
    5 + 5 * 2 -> 15
    (5 + 5) * 2 -> 20
    
### Strings
    Can use single or double quotes. 
        'apple' or "apple"
    'He\'s correct'
    
    To preserve long strings on new lines use triple quotes!
        '''He's correct'''
        """He's correct"""
    
    str(5) -> '5'
    'Hello' + 'There' -> HelloThere
    "Hello " + "there" -> Hello there
    'a' + str(5) -> a5
    '=' * 20 -> ======================
    status_message = "Hey, we have {} people using the site right now"
    print(status_message.format(7))
    
####Split

    When we want to break a string into a list based on something that repeats in the string, we use the .split() method. By default, .split() splits the string on whitespace (i.e. spaces, tabs, newlines, etc). If you want to split based on something else, give that something else to the .split() method. Let's go to an example!
    
    "Hello there".split() produces ["Hello", "there"].
    
    "name;age;address".split(";") produces ["name", "age", "address"].

####Join
    
    The str type's .join() method lets us combine all of the items in a list into a string with a particular string between each pair of items. How about an example?
    
    my_favorite_colors = ["green", "black", "silver"]
    my_string = "My favorite colors are "
    my_string + ", ".join(my_favorite_colors)
    The above would produce "My favorite colors are green, black, silver".
    
    You cannot join things that aren't strings. Doing ", ".join(5, 10, 15) will give you an exception.
    
    flavors = ['chocolate', 'cherry', 'mint']
    ', '.join(flavors)  -> 'chocolate, cherry, mint'
    "My favorite flavors are: " + ', '.join(flavors) -> 'My favorite flavors are: chocolate, cherry, mint'
    'My favorite flavors are: {}'.format(', '.join(flavors)) -> 'My favorite flavors are: chocolate, cherry, mint'

### Lists
    You can create a list with the list() function or using two square brackets ([]).

    You can use the plus sign to add items into a list so long you add two lists together (e.g. [1, 2, 3] + [4, 5] would create [1, 2, 3, 4, 5]. [1, 2, 3] + 4 would create a TypeError). You can multiply a list by an integer and get back the content of the list as many times as the value of the integer (e.g. [1, 2] * 2 would produce [1, 2, 1, 2]).
    
    You can use the .append() method to add a single item to the end of a list.
    
    You can use the .extend() method to add every item from one list to another list.
    
    You can use the .remove() method to remove a particular value from a list.
    
    my_list = [1, 2, 3, 4, 5, 6]
    len(my_list) -> 6
    my_list += [7, 8] -> [1, 2, 3, 4, 5, 6, 7, 8]
    my_list * 2 -> [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
    
### Bool
    
    The bool() function will tell you whether something (a variable, a comparison (next video!), or anything else) evaluates to true or false. You won't find this used a lot in every day Python programming but it's super-handy for testing your assumptions when you're still learning.
    Python has seven comparators, or comparison operators. Each of them returns True or False. Here they are:
    
    Operator	Comparison
    ==	A is equal to B
    !=	A is not equal to B
    <	A is less than B
    >	A is greater than B
    <=	A is less than, or equal to, B
    >=	A is greater than, or equal to, B
    is	A has the same memory address as B
    
### Logic
        
    Python if blocks always start the same way:
    
    if a < b:
        print("A is tiny!")
    It's always the keyword if followed by the condition. In this case, the condition is a < b but your conditions will be different. Then comes a colon (:), a return, and the body of the if is indented.
    
    If you want something to happen when the condition is False, you'd put that into an else: block, which is just the word else followed by a colon.
    
    If you need another possible condition, use the elif block, like so:
    
    elif a == b:
        print("A and B are equivalent!")
    The elif block is built exactly like the if block but with elif instead of if. All of your elif blocks must come before any else blocks.
    
    EXAMPLE: 
        age = 14
        admitted = None
        if age >= 13:
            admitted = True
        else:
            admitted = False
    
    in returns whether or not a value is inside of a container. We can use this to see if, for example, a smaller string is in a bigger string or if a certain item is in a list.

    Examples
    
    "java" in "javascript" would give back True
    
    5 in [3, 4, 1] would give back False

### Loops

    Python has two loop types, for and while.
    
    for loops run a certain number of times and then end themselves. while loops, on the other hand, run until their condition, like an if has, turns False. If it helps, you can think of while loops as repetitious ifs.
    
    For loop
    
    numbers = [1, 2, 3, 4]
    doubles = []
    for number in numbers:
        doubles.append(number*2)
    This loop will run four times because there are four items in the numbers list. On each iteration of the loop, we're calling the value at the current index number.
    
    While loop
    
    start = 99
    while start:
        print("{} bottles of milk on the wall, {} bottles of milk.".format(start, start))
        print("Take one down and pour it on some cereal.")
        start -= 1
        print("{} bottles of milk on the wall.".format(start))
    This while loop will print out something like the traditional "99 bottles" song many of us used to annoy our parents on road trips. The loop stops when start becomes something False, which will happen when it's reduced to 0.
    
    break
    
    You can stop a loop early by using the keyword break.
    
    for letter in "abcdef":
        if letter == "c":
            break
        print(letter)
    This loop will print "a" and "b" and then stop because of the break when letter is "c".
    
    break can only be used inside of a loop.
    
    continue
    
    for letter in "abcdef":
        if letter == "c":
            continue
        print(letter)
    Nearly the same loop but this one will print "a", "b", "d", "e", and "f". It skips "c" because of the continue, which causes the loop to immediately move on to the next step in the loop.
    
    Like break, continue can only be used inside of a loop.
    
    else
    
    And, finally, we have the else: block for both loops. If the loop ends naturally, meaning it doesn't have a break triggered and no exceptions happen, the loop's else block will happen, if one exists. The else block is entirely optional, just like with if.
    
    for num in [2, 4, 6]:
        print(num*10)
    else:
        print("That's all of the numbers, multiplied by 10.")
    This loop can't throw an exception and doesn't have a break in it, so the else will always happen.

### Input
    We use the input() function to get information from a user.
    
    input("WHAT is your favorite color? ") takes an optional prompt to use when you need to ask the user a particular question. Python doesn't add any space at the end of the prompt, though, so remember to do that yourself.
    
    The value that comes in from input() is always a string, so if you need a number or something else, you'll need to convert it afterward.

### Exceptions
    We handle exceptions with two blocks, try and except.

    The try block is just that, the word try followed by a colon. Inside of the block, indented, is the code that you think might 'cause an issue.
    
    try:
        num = int(input("What is the airspeed velocity of an unladen swallow? "))
    Now, someone might not give us a number for that and that would cause a ValueError. So let's catch it!
    
    except ValueError:
    This block will only trigger if the code in the try caused a ValueError. If the code in the try triggered a TypeError instead, though, this code would never run.
    
    You'll want to create an except block for every type of exception your try block might cause.
    
    Finally, you'll probably want an else block. This block will happen if your try didn't cause any exceptions.
    
    Example
    
    try:
        speed = int(input("What is the airspeed velocity of an unladen swallow? "))
    except ValueError:
        print("What? I don't kno-oooooooooooooooo!")
    else:
        print("I think a swallow could go faster than {}.".format(speed))

### Functions 
    syntax:
        def my_function():
            print('this is my function')

