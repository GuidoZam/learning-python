from operator import truediv

# Implicit variable type
stringVar = "this is a string variable"
# Explicit variable type
s: str = "this is another string"

intVar = 42
i: int = 4

boolVar = True

dictionaryVar = dict()
dictionaryVar[0] = 1
dictionaryVar[1] = 2

# Multiple assignment
# All with the same value
a = b = c = 33

print(a, b, c)

# Different values
d,e,f = 1, "two", 3

print(d, e, f)

# Variables can be deleted
del e

# String operations
sourceString = "Hello World"
print(sourceString)         # Prints the complete string
print(sourceString[0])      # Prints first character of the string
print(sourceString[6:11])   # Prints characters of the string starting from 6th till 11th
print(sourceString[3:])     # Prints characters of the string starting from 3rd character
print(sourceString * 3)     # Prints the string three times

# List operations
list = ['test', 2, 30.3, "test2"]
print(list)         # Prints the complete list
print(list[0])      # Prints first element of the list
print(list[1:3])    # Prints elements of the list starting from 2nd till 3rd
print(list[2:])     # Prints elements of the list starting from 3rd element
print(list * 2)     # Prints the contents of the list twice

# Tuple operations
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print(tuple)        # Prints the complete tuple
print(tuple[0])     # Prints first element of the tuple
print(tuple[1:3])   # Prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])    # Prints elements of the tuple starting from 3rd element
print(tuple * 2)    # Prints the contents of the tuple twice

# Dictionary operations
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code': 6734, 'dept': 'sales'}

print(dict['one'])          # Prints value for 'one' key
print(dict[2])              # Prints value for 2 key
print(tinydict)             # Prints complete dictionary
print(tinydict.keys())      # Prints all the keys
print(tinydict.values())    # Prints all the values