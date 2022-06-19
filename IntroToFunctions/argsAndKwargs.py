def multiply(num1,num2):
    return num1*num2

print("product:", multiply(2,3)) 

def multiplyThreeNumbers(num1, num2, num3):
    return num1*num2*num3

print("product:",multiplyThreeNumbers(1, 2, 3))

# To avoid specifing multiple arguments for function you can write the function this way
def multiplyNumbers(*numbers): # *numbers specify that it is an *args variable
    # *args are non keyword arguments
    product=1
    for n in numbers:
        product*=n
    return product

print("product:",multiplyNumbers(4,4,4,4,4,4)) 

# Using keyword arguments
def makeSentence(**words): # *words specify it is an **kwargs variable
    sentence=''
    for word in words.values():
        sentence+=word
    return sentence

print('Sentence:', makeSentence(a='Kwargs ',b='are ', c='awesome!'))

# Another example with **kwargs
def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(key, value))
    return result

print(whatTechTheyUse(Google='Angular', Facebook='React', Microsoft='.NET'))

# It is possible to use both *args and *kwargs in the same function
def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)

printingData('007', 'agent', firstName='James', lastName='Bond') 
