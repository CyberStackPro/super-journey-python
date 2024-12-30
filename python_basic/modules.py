# Modules
# A module is a file with some Python code. We use modules to break up our
# program into multiple files. This way, our code will be better organized. We won’t
# have one gigantic file with a million lines of code in it!
# There are 2 ways to import modules: we can import the entire module, or specific
# objects in a module.

# importing the entire converters module
import converters
converters.kg_to_lbs(100)

# importing one function in the converters module
from converters import kg_to_lbs
kg_to_lbs(5)

# Packeges
# A package is a directory with __init__.py in it. It can contain one or more modules.

# importing the entire sales module
from ecommerce import sales
sales.calc_shipping()   

# importing one function in the sales module
from ecommerce.sales import calc_shipping
calc_shipping()

# Python Standard Library
# Python comes with a huge library of modules for performing common tasks such as
# sending emails, working with date/time, generating random values, etc.
# Random Module
import random
random.random()  # returns a float between 0 to 1
random.randint(1, 6) # returns an int between 1 to 6
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members) # randomly picks an item


# Pypi
# Python Package Index (pypi.org) is a directory of Python packages published by
# Python developers around the world. We use pip to install or uninstall these
# packages.
# pip install openpyxl

# pip uninstall openpyxl