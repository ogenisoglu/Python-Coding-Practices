from random import shuffle
a=["A","L","A","F","R","A","N","G","A"]
new=[a.copy()]
b=[]
i=0
while len(new)<15120:
    shuffle(a)
    if a in new:
        continue
    else:
        new.append(a.copy())
        i+=1
        print(i)
neww=[]
for i in range(len(new)):
    for j in range(len(new[i])-1):
        if new[i][j+1]=="A" and new[i][j]=="A":
            neww.append(new[i])
            break
def diff(first, second):
        return [item for item in first if item not in second]
print(diff(new,neww))