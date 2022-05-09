def thisIsAFunction():
    """
    This is a description of the function
    """
    print("Hello from function!")
    
thisIsAFunction()

def isBiggerThan5(n):
    """This is a summary for isBiggerThan5

    Args:
        n (int): The number to compare to 5
    """
    if (n > 5):
        print(n, "is bigger than 5")
    else:
        print(n, "is lower than 5")

isBiggerThan5(3)
isBiggerThan5(42)