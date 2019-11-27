from gen_spisok import gen_sp2
print("Введите i и j: \n")
a=int(input())
b=int(input())
print("Введите s: \n")
s=int(input())
spisok=gen_sp2(a,b)
print("Сам список")
for i in range(a):
    for j in range(b):
        print("{:4d}".format(spisok[i][j]),end=' ')
    print()
sum_a = 0
sum_b = 0
for j in range(b):
    sum_a += spisok[2][j]
for i in range(a):
    sum_b += spisok[i][s-1]
print("Ответы на задания:","\n","а)",sum_a,"\n","б)",sum_b)    
            
            
    
