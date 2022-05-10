def describe(v1, v2):
    return print(v1, "is of type", type(v1), " -> ", v2, "is of type", type(v2))

# Converts x to an integer. base specifies the base if x is a string	
# int(x [,base])
v = "4"
describe(v, int(v))

# Converts x to a long integer. base specifies the base if x is a string
# long(x [,base] )
#print(long("94349"))

# Converts x to a floating-point number
# float(x)
f = "4.2"
describe(f, float(f))

# Creates a complex number
# complex(real [,imag])
c = "4.54"
describe(c, complex(c))

# Converts object x to a string representation
# str(x)
s = 97
describe(s, str(s))

# Converts object x to an expression string.
# repr(x)
r = {"test":3}
describe(r, repr(r))

# Evaluates a string and returns an object
# eval(str)
stringObject = "{'test':'this is a test property'}"
o = eval(stringObject)
describe(stringObject, o)
print("The property value is:", o["test"])

# Converts s to a tuple
# tuple(s)
tupleString = "tuple string"
t = tuple(tupleString)
describe(tupleString, t)

# Converts s to a list
# list(s)
listString = "Python"
l = list(listString)
describe(listString, l)

# Converts s to a set
# set(s)
sourceList = [ 3, 4, 1, 4, 5 ]
set = set(sourceList)
describe(sourceList, set)

# Creates a dictionary. d must be a sequence of (key,value) tuples
# dict(d)
dictVal = {"yy":"John","zz":"Doe"}
describe(dictVal, dict(dictVal))

# Converts s to a frozen set, frozen sets are immutable
# frozenset(s)
frozenSet = frozenset(set)
describe(set, frozenSet)

# Converts an integer to a character
# chr(x)
i = 76
describe(i, chr(i))

for x in range(33,40):
    print(x," - ", chr(x))

# Converts a single character to its integer value
# ord(x)
for x in range(41,49):
    print(chr(x)," - ", ord(chr(x)))

# Converts an integer to a hexadecimal string
# hex(x)
for x in range(49,55):
    print(hex(x)," - ", chr(x))

# Converts an integer to an octal string
# oct(x)
for x in range(56,63):
    print(chr(x)," - ", oct(x))