listOfThings = ["qwer", 123, "2"]
print(listOfThings)
print(type(listOfThings[2]))

print(listOfThings[:2]) # display first two items on the list
print(type(listOfThings[:2]))

print(dir(list))

listOfThings.append("add Me")
print(listOfThings)

print(help(listOfThings.remove))
listOfThings.remove(123)
print(listOfThings)
