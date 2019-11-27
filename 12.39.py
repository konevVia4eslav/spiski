from gen_spisok_for12_39 import gen_sp2
a=25
b=36
spisok=gen_sp2(a,b)
print("Сам список")
for i in range(a):
    for j in range(b):
        print("{:1d}".format(spisok[i][j]),end=' ')
    print()
sum_a = 0    
for j in range(b):
    if spisok[11][j] == 1:
        sum_a += spisok[11][j]
print("Ответ:","\n",sum_a)
