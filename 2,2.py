from random import randint
d1 = []
d = int(input('dlinna: '))
v = int(input('vysota: '))
for j in range(d):
    d2 = []
    for i in range(v):
        d2.append(randint(1,100))
    
    print(d2)