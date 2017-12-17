# Create a function that converts Celsius degrees to Fahrenheit. The formula to convert Celsius to Fahrenheit is F = C × 9/5 + 32.

def celsius_to_fahrenheit(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit

# print(celsius_to_fahrenheit(10))

# ------------------------------------

# Calculate Length

# def lenString(someString):
def lenString():
    someString = input("Write something: ")
    return "Length of your string is: " + str(len(someString))

# print(lenString("qweretyuio"))
print(lenString())
