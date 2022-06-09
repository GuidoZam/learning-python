import datetime

name = "Jane"
surname = "Doe"
age = 34
person = { name: "John", surname: "Doe" }
address = { "address": "Some street", "number": 42, "city": "Gotham City" }

def toUpper(sourceString: str):
    return sourceString.upper()

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # The str() function returns a user-friendly description of an object
    # The __str__() is called inside the str() function
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    # The repr() method returns a developer-friendly string representation of an object
    # The __repr__() is called inside the repr() function
    def __repr__(self):
        return f'Person{{"{self.first_name}","{self.last_name}","{self.age}"}}'

# %-formatting
# This is not the best option when there are multiple variables
print("Hello! My name is %s." % name)
print("Hello again, I'm %s %s and I'm %s years old." % (name, surname, age))

# str.format()
# This is not the best option either when there are long strings and multiple parameters
print("Hello! I'm {} {} and I'm {} years old.".format(name, surname, age))
print("Hello! I'm {1} {0} and I'm {2} years old.".format(name, surname, age))
print("Hello! I'm {firstName} {lastName} and I'm {age} years old.".format(firstName = name, lastName = surname, age = age))
print("I live in {address} at number {number} in {city}.".format(**address))

# f or F strings
print(f"I'm {name} {surname}.")
print(F"The power of {age} is {age * age}.")
print(f"My name in uppercase is {toUpper(name)}.")

# multiline f string
print(
    f"Hi! "
    f"I'm {name} {surname}."
)

print(
    f"Hi! " \
    f"I'm {name} {surname}."
)

print(f"""
    Hi! 
    I'm {name} {surname} and I'm formatted.
    """
)

# Use of str and repr
dummyPerson = Person("Mario", "Super", "38")
print(f"{dummyPerson}")
print(f"{repr(dummyPerson)}")
print(f"{dummyPerson!r}")

# str and repr on date time
today = datetime.datetime.now()
print(str(today))
print(repr(today))