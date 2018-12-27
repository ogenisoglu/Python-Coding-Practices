#palindroms are strings that is symmetric
#example: "ey edip adanada pide ye" "racecar"
while True:
    x=str(input())
    b=len(x)
    a=0
    for i in range(len(x)):
        if x[i]==x[len(x)-1-i]:
            a=a+1
    if a==len(x):
        print("Palindrome")
    else:
        print("Not palindrome")
