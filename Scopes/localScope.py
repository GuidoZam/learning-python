
def func():
    b = "This is a value"
    print(b) # will print b
 
func()
print(b) # nameError will be thrown as b exists only in func()'s local scope
