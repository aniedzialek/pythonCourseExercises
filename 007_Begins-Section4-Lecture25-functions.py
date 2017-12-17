def minutes_to_hours(someOtherNonDefaultArgument, minutes = 80):    # default argument
    # first go the non default arguments, then default ones, otherwise you'll get a syntax error

    hours = minutes % 60
    restMinutes = minutes - 60
    return hours, restMinutes

print(minutes_to_hours(70))
print(type(minutes_to_hours(70)))

# ---------------------------------

def power(numberToPowerUp):
    return numberToPowerUp**2

print(power(10.2))
print(type(power(10.2)))
