city = "London"
def withoutGlobal():
    city = "Paris"
def withGlobal():
    """ 
    This function changes the global variable city to Paris.
    """
    global city
    city = "Paris"

withoutGlobal()
print(city)

withGlobal()
print(city)

print("__var".isidentifier())
print(withGlobal.__doc__)