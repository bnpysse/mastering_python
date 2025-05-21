print(eval("5+2*3-1/2"))
print(eval("pow(2,4)-5+max(10,5)"))

var = 'computer'
print(id(var))
del(var)
try:
    print(var)
except NameError:
    print("NameError: name 'var' is not defined")