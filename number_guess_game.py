""" Ömer Genişoğlu 240201049"""
import random
S=100                                                                       #Save the score
begin=str(input("Begin? "))                                                 #Take the begin number from user
while not begin.isnumeric():                                                #Check the begin number is valid or not
    begin=str(input("Enter a numberic value for begin: "))                  
begin=int(begin)                                                            #Change string to integer
end=str(input("End? "))                                                     #Take the end number from user
while True:
    try:
        end=int(end)
        if end<begin+5:                                                     #Check the end number is valid or not 
            end=str(input("Enter a value minimum 5 grater than begin: "))
            continue
        else:
            break
    except:
        end=str(input("Enter a numeric value:\n"))
a="l"
target=random.randint(begin,end)
N=(end-begin+1)//5                                                          #Calculate how many guesses will have user
while target!=a and S>0 and N>0:
    if N>20:								                                #Max range is 20
        N=20                                                                #If guess is not equal to target loop will ask every turn to user
    print("\nTarget is in",[begin,end],"\nYou have",N,"guesses...")         #Print informations
    for i in range(N):                                                      #For loop will repeat as much as N(guess)
        while True:                                                          
            a=str(input())
            try:
                a=int(a)
                if a<begin or a>end:
                    print("Enter a value in specified range:")              #Try-except helps to determine the entry is number or not
                    continue
                else:
                    break
            except:
                print("Enter a numeric value:")
        N=N-1                                                               #Every turn guess number is decreasing by one, because some instructions will use it
        if a==target:
            print("Right guess! Score:",S)                                  #It exits from for loop if guess is true
            c=str(input("Press enter to exit."))
            break
        elif S==0:
            break
        elif N==0:                                                          #If this is the last turn of for loop N must be 0
            print("Wrong guess!")                                           #Begin or end values change every last of for loops
            if target-begin>end-target:
                begin=(end+begin)//2
                S=S-5
            else:
                end=(end+begin)//2
                S=S-5
        else:
            print("Wrong guess!")                                           #Last of a for turn, it continues because N is still bigger than 0
            S=S-5
    N=(end-begin)//5                                                        #Every while turn, N is updated
if a!=target:                                                               #If user lost, print it
    print("You lost! The target was "+str(target)+".")
    c=str(input("Press enter to exit."))