# EXAMPLE
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"
import random

def random_item(value):
    output = value[random.randint(0, len(value)-1)]
    return output


print(random_item('rich'))