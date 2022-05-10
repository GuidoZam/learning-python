a = "This is a test string"
if "test" in a:
    print("string contains test!")

if ("test" in a) is True:
    print("It's funny because it is true!")

if False:
    print("This is never reached")
elif False:
    print("Also this will never be reached")
else:
    print("This is currently reached!")

multiplyBy2 = lambda n: n * 2
print(multiplyBy2(9))