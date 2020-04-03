from random import randint
n = list(randint(-1000, 1000) for x in range(20))
print (n)
result = []
for i in n:
    if ((i % 11) == 0):
        result.append(i)
a = sorted(result, reverse = True)
print( "кратні 11 = " , (a))