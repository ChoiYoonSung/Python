import random
mine = input("가위/바위/보\n>")
com = ""
result = ""

rnd = random.random()
if rnd >= 0.66:
    com = "가위"
elif rnd < 0.66 and rnd > 0.33:
    com = "바위"
else:
    com = "보"

if com == "가위" and mine == "가위":
    result="비김"
elif com == "가위" and mine == "바위":
    result="이김"
elif com == "가위" and mine == "보":
    result="짐"

if com == "바위" and mine == "가위":
    result="짐"
elif com == "바위" and mine == "바위":
    result="비김"
elif com == "바위" and mine == "보":
    result="이김"

if com == "보" and mine == "가위":
    result="이김"
elif com == "보" and mine == "바위":
    result="짐"
elif com == "보" and mine == "보":
    result="비김"


# if com == mine:
#     result = "비김"
# elif com == "가위":
#     if mine == "바위":
#         result = "이김"
#     else:
#         result = "짐"
# elif com == "바위":
#     if mine == "보":
#         result = "이김"
#     else:
#         result = "짐"
# elif com == "보":
#     if mine == "가위":
#         result = "이김"
#     else:
#         result = "짐"

print("mine : " + mine)
print("com : " + com)
print("결과 : " + result)