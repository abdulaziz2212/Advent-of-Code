import re
with open(r'D:\CP\robocontest\adventofcode\test.txt','r') as file:
    txt=file.read()
pattern=r"mul\((\d+),(\d+)\)"
pattern2=r"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))"
matches=re.findall(pattern,txt)
match2=re.findall(pattern2,txt)
sum1=0
sum2=0
enabled=True
for nums in matches:
    sum1+=int(nums[0])*int(nums[1])
print(sum1)

for sec in match2:
    part,num1,num2=sec
    if part=="don't()":
        enabled=False
    elif part=='do()':
        enabled=True
    elif enabled and num1 and num2:
        sum2+=int(num1)*int(num2)
print(sum2)