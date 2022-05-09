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


# Converts s to a tuple
# tuple(s)


# Converts s to a list
# list(s)


# Converts s to a set
# set(s)


# Creates a dictionary. d must be a sequence of (key,value) tuples
# dict(d)


# Converts s to a frozen set
# frozenset(s)


# Converts an integer to a character
# chr(x)


# Converts an integer to a Unicode character
# unichr(x)


# Converts a single character to its integer value
# ord(x)


# Converts an integer to a hexadecimal string
# hex(x)


# Converts an integer to an octal string
# oct(x)