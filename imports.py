# This is a simple program to show how to import modules in Python.

import random
# These are called generic imports. They import the entire module and you can access its functions using the module name.
print(random.randint(1, 10))  # This will print a random integer between 1 and 10.

from math import sqrt
# This is a specific import. It imports only the sqrt function from the math module, so you can use it directly without the module name.
print(sqrt(16))  # This will print the square root of 16.

from datetime import *
# This is a wildcard import. It imports all functions and variables from the datetime module, so you can use them directly without the module name.
# However, it's generally not recommended to use wildcard imports because it can lead to confusion and conflicts with other modules.
# It's better to use specific imports or generic imports to keep your code clear and organized.

print(date.today())  # This will print today's date.