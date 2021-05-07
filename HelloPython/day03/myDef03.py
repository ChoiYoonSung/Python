def addmin(a,b):
    return a+b, a-b

sum,min = addmin(5,6)
min2 = addmin(10,7)[1]

print(sum, min)
print(min2)