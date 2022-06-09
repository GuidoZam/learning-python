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

# Function with return value
def multiplyByTwo(n):
    return n * 2

varToMultiply = 7
print(varToMultiply,"* 2 =", multiplyByTwo(varToMultiply))

# Function that returns a tuple
def getTuple():
    stringValue = "This is a string"
    numberValue = 42
    return stringValue, numberValue

value1,value2 = getTuple()
print(getTuple())
print(value1)
print(value2)

# Function with lambda
def compareInts(a,b) -> bool:
    return a == b

print(compareInts(3,4))

def functionWithDefaults(name = "John", surname = "Doe"):
    """This is a function that shows how to use defaults

    Args:
        name (str, optional): _description_. Defaults to "John".
        surname (str, optional): _description_. Defaults to "Doe".
    """
    print(f"Hi! I'm {name} {surname}.")

functionWithDefaults()
functionWithDefaults("Jane")
functionWithDefaults("Bruce", "Wayne")
functionWithDefaults(surname="Super", name="Mario")

def functionWithMultipleArguments(*foods):
    for food in foods:
        print(food)

functionWithMultipleArguments("Strawberry", "Apple", "Banana", "Ananas")

def functionWithMultipleKeyArguments(**animals):
    for animal in animals.items():
        print(animal)

functionWithMultipleKeyArguments(Lion="Carnivore", Elephant="Herbivore", Gorilla="Omnivore")

def functionMixedArguments(*foods, **animals):
    for food in foods:
        print(food)
    for animal in animals.items():
        print(animal)

functionMixedArguments("Strawberry", "Apple", "Banana", Lion="Carnivore", Elephant="Herbivore")