from random import randint

lista = []

for i in range(100):
    szam:int = randint(200, 1999) * 5
    lista.append(szam)
    print(lista[i], end=' ')
    if (i+1) % 10 == 0: print()

print(f'lista elemeinek összege: {sum(lista)}')

db_4K5K:int = 0
sum_4K5K:int = 0
for e in lista:
    if 4000 <= e < 5000:
        db_4K5K += 1
        sum_4K5K += e
print(f'[4K,5K) közötti elemek átlaga: {sum_4K5K / db_4K5K}')

maxi = 0
for i in range(1, len(lista)):
    if lista[i] > lista[maxi]:
        maxi = i
print(f'a legnagyobb elem: lista[{maxi}] = {lista[maxi]}')
print(f'sor:    {maxi // 10 + 1}')
print(f'oszlop: {maxi % 10 + 1}')

db_25K:int = 0
sum_25K:int = 0

while sum_25K < 25000:
    sum_25K += lista[db_25K]
    db_25K += 1
print(f'összesen {db_25K} elemet kell összeadnom a lista elejétől, hogy elérjem a 25.000 összeget!')