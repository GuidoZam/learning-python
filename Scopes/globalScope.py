a = 10
def func1():
    # as a does not exist in the local scope of func1(), according to the LEGB rule, 
    # the interpreter looked into the global scope
    print("inside func1 ", a)
 
func1()
print("at global scope ", a)