dickt = {'001':['BMW','chort'],'002':['tesla','petrenko'], '003':['toyota', 'kernes']}
nomer = input('введіть номер ')
dell = dickt.get(nomer) 
numb = dickt.keys()
length = len(numb)
print ("Прізвище власника - ",dell,"Статистика - ", numb,"Кількість ", length)