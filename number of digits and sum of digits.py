#ömer genişoğlu
x=int(input())
a=0
b=5
while (x//(10**a))>0:
    a=a+1
print(a)
summ=0
for i in range(a):
    c=x//(10**(a-1))
    x=x-c*(10**(a-1))
    summ=summ+c
    a=a-1
input(summ)

    
