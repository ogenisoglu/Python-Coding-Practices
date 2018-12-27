x=int(input())
fibo=1
fibo_last=1
fibo_lastto=1
for i in range(x-2):
    fibo=fibo_last+fibo_lastto
    fibo_lastto=fibo_last
    fibo_last=fibo
input(fibo)
