a = int(input("첫 숫자를 입력하시오\n>"))
b = int(input("끝 숫자를 입력하시오\n>"))
arr = range(a, b+1)
result = 0

for i in arr:
    result += i

print("모든 수의 합은 {}입니다.".format(result))