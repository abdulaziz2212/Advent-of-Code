#part1
count=0
for i in range(1000):
    
    a=list(map(int, input().split()))
    #adjacent dif
    if all(abs(a[i + 1] - a[i]) in {1, 2, 3} for i in range(len(a) - 1)): 
        # monotonicity
        if all(a[i] < a[i + 1] for i in range(len(a) - 1)) or all(a[i] > a[i + 1] for i in range(len(a) - 1)):  
            count += 1
    
print(count)

#part2

count=0
for i in range(1000):
    a=list(map(int, input().split()))
    #adjacent dif
    if all(abs(a[i + 1] - a[i]) in {1, 2, 3} for i in range(len(a) - 1)):  
        #monotonicity
        if all(a[i] < a[i + 1] for i in range(len(a) - 1)) or all(a[i] > a[i + 1] for i in range(len(a) - 1)):  
            count += 1
            continue

    for i in range(len(a)):
        modList=a[:i]+a[i+1:]  #removing one element
        if all(abs(modList[i + 1] - modList[i]) in {1, 2, 3} for i in range(len(modList) - 1)):  
            if all(modList[i] < modList[i + 1] for i in range(len(modList) - 1)) or all(modList[i] > modList[i + 1] for i in range(len(modList) - 1)):
                count += 1
                break

print(count)
