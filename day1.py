#part1
a=[]
b=[]
while True:
    try:
        x,y=map(int, input().split())
        a.append(x)
        b.append(y)
    except:
        a.sort()
        b.sort()
        sum=0
        for i in range(len(a)):
            sum+=abs(a[i]-b[i])
        print(sum)
        print(len(a))
        
#part2
from collections import defaultdict
a=[]
b=defaultdict(int)
while True:
    try:
        x,y=map(int, input().split())
        a.append(x)
        b[y]+=1
    except:
        sum=0
        for i in a:
            if i in b.keys():
                sum+=i*b[i]
        print(sum)

