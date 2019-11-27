from gen_spisok import gen_sp2
print("Введите i и j: \n")
a=int(input())
b=int(input())
print("Введите k: \n")
s=int(input())
spisok=gen_sp2(a,b)
print("Сам список")
for i in range(a):
    for j in range(b):
        print("{:4d}".format(spisok[i][j]),end=' ')
    print()
sum_a = 0
sum_b = 0
for i in range(a):
    sum_a += spisok[i][1]
for j in range(b):
    sum_b += spisok[s-1][j]
print("Ответы на задания:","\n","а)",sum_a,"\n","б)",sum_b)
