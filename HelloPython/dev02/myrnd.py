import random
from dask.array.random import randint

mine = input("홀/짝을 선택하세요")
com = "" 
com2 = ""
result = "" 

rnd = randint(1,3)%2
rand = random.random()
if rnd == 1:
    com = '홀'
else:
    com = '짝'
    
if mine == com:
    print("com1 답 : " + com +", 맞췄습니다.")
else:
    print("com1 답 : " + com +", 틀렸습니다.")
    
#-------------
if rand < 0.5:
    com2 = "홀"
else:
    com2 = "짝"

if mine == com2:
    result = "이김"
else:
    result = "짐"

print("com : " + com2)
print("mine : " + mine)
print(result)