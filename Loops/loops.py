print("For loop")
for n in range(5):
    print("Value is " + str(n))

print("While loop")
i = 1
while(i <= 5):
    print("Value is " + str(i))
    i = i + 1

print("For loop with break")
for n in range(10):
    print("Value is " + str(n))
    if n == 4:
        break

print("For loop with continue")
for n in range(10):
    if n < 5:
        continue
    print("Value is " + str(n))