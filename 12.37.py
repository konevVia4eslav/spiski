from gen_spisok_for12_37and12_40 import gen_sp2
a=11
b=4
spisok=gen_sp2(a,b)
print("Сам список")
for i in range(a):
    for j in range(b):
        print("{:3d}".format(spisok[i][j]),end=' ')
    print()
sum_a = 0    
for j in range(b):
    sum_a += spisok[4][j]
print("Ответ:","\n",sum_a)    
