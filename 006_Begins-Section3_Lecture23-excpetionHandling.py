def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:                  # Error type is optional
        return "You are dividing by zero"      # without return it will print out the text and then NONE as for any function without return statement

print(divide(1,0))
print(divide(1,1))
