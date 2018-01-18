# Create a function that converts Celsius degrees to Fahrenheit. The formula to convert Celsius to Fahrenheit is F = C × 9/5 + 32.

def celsius_to_fahrenheit(celcius):
    if celcius > -273.15:
        fahrenheit = celcius * 9/5 + 32
        return fahrenheit
    else:
        return "Temperature you specified is below absolute zero. Please give a higher number."

# print(celsius_to_fahrenheit(10))
print(celsius_to_fahrenheit(-273.03))

# ------------------------------------

# Calculate Length

# def lenString(someString):
def lenString():
    someString = input("Write something: ")
    return "Length of your string is: " + str(len(someString))

# print(lenString("qweretyuio"))
# print(lenString())
