dan = int(input("출력할 구구단은?\n>"))

arr = range(1,10)

for i in arr :
    print(str(dan)+ " * " + str(i) + " = " + str(dan*i))