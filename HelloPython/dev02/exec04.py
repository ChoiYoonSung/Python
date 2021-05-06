a = int(input("첫 숫자를 입력하시오\n>"))
b = int(input("끝 숫자를 입력하시오\n>"))
arr = range(a,b+1)
result = 0;

for i in arr:
    if i%2 == 0:
        result += i
print("짝수의 합은 " + str(result) + " 입니다.")