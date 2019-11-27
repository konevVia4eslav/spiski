from gen_spisok_for12_38 import gen_sp2
a=20
b=5
spisok=gen_sp2(a,b)
print("Сам список")
for i in range(a):
    for j in range(b):
        print("{:3d}".format(spisok[i][j]),end=' ')
    print()
sum_a = 0    
for j in range(b):
    sum_a += spisok[2][j]
print("Ответ:","\n",sum_a)
