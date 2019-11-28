from gen_spisok import gen_sp2
print("Введите i и j: \n")
a=int(input())
b=int(input())
spisok=gen_sp2(a,b)
print("Сам список")
for i in range(a):
    for j in range(b):
        print("{:4d}".format(spisok[i][j]),end=' ')
    print()
min_a = 0
min_b = 0
for j in range (b):
    if spisok[4][j] < min_a:
        min_a = spisok[4][j]
for i in range (a):
    if spisok[i][3] < min_b:
        min_b = spisok[i][3]
print("Ответы на задания:","\n","а)",min_a,"\n","б)",min_b)
