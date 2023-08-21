# import math
# print("1")
# print('我是”小明“')
# a = "10086"
# print("a是"+a)
# print(math.sin(1))

# import math
# a = -1
# b = -2
# c = +3
# print((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
# print((-b - math.sqrt(b**2 - 4*a*c))/(2*a))

# a = {"小A":"1234","小B":"4321"}
# print(a["小A"])
#
# a = "abcdef"
# a += input()
# print(a)

n = int(input())
map = {}
for i in range(n):
    temp = ""
    for y in range(8):
        temp += input()
    if temp not in map:
        map[temp] = 1
    else:
        map[temp] += 1
    print(map[temp])