# def string_length(mystring):
#     return len(mystring)
#
# Your task is to modify the function so that if an integer is passed as an input, the function should output a message like "Sorry integers don't have length".

def string_length(mystring):
    if (type(mystring) == int):
        return "Sorry, integers don't use length"
    elif (type(mystring) == float):
        return "Sorry, floats don't use length"
    else:
        return len(mystring)

# print(string_length(input("Write something: ")))  # in this case all input is treated as string

print(string_length(10))

# --------------------------------
