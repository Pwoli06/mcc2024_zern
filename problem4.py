#Problem4

import sys
sys.stdout = open('c:/Code/Competitive Programming/mcc2024/output4.txt', 'w')
sys.stdin = open('c:/Code/Competitive Programming/mcc2024/input4.txt', 'r')

n = int(input())
li = []
li_sorted= []
x_choice = []
y_choice = []
j = 0
sum_x = 0
sum_y = 0

for i in range(n):
    x, y = map(int, input().split())
    li.append([x+y, x, y])
    li_sorted = sorted(li,reverse=True)


for i in range(n):
    if i %2 == 0:
        sum_x += li_sorted[i][1]
    else:
        sum_y += li_sorted[i][2] 

print(sum_x-sum_y)

#print(li) 
#print(li_sorted)

"""     x = list(map(int, input().split()))
    li.append(x)
    li_sorted.append(li[i][0]+li[i][1])
    li_sorted.sort(reverse=True) """


""" for i in range(n):
    if i %2 == 0:
        x_choice.append(li_sorted[i])
    else:
        y_choice.append(li_sorted[i])

print(x_choice, y_choice)

for i in range(n):
    if li[i][0] + li[i][1] in x_choice:
        sum_x += li[i][0]
    elif li[i][1] + li[i][0] in y_choice:
        sum_y += li[i][0]

print(sum_x+sum_y) """


""" turn = 1 #turn = 1 for x, 0 for y

choice = 0
x = 0
y = 0
sum_x = 0
sum_y = 0

num = 0

print(li)

while True:
    if turn == 1:
        turn = 0
        for i in range(n):
            num = li.append(li[i][0]+li[i][1])
            print (num)
            if x < num:
                x = li[i]
                count = i
                sum_x = sum_x + x[0]
        li.pop(count)        
        n -= 1 
    if turn == 0:
        turn = 1
        for i in range(n):
            if y < (li[i][0]+li[i][1]):
                y = li[i]
                count = i
                sum_y = sum_y + y[1]  
        li.pop(count)        
        n -= 1 

print(sum_y-sum_x)


for i in range(n):
    x = list(map(int, input().split()))
    temp.append(x) 
    li.append(temp[i][0]-temp[i][1])   
print (temp)
print (li)
li.sort(reverse=True)

x = []
y = []
z = int(n/2)

for i in range(z):
    x.append(temp[i])

for i in range(z,n):
    y.append(temp[i])
    

print(x)
print(y)

sum_x = 0
sum_y = 0

for i in range(z):
    sum_x = 





#choose the biggeest diffrence

turn = 1
x = 0
y = 0

x_index = 0
y_index = 0

sum_x = 0
sum_y = 0

for i in range (n):
    if x <= li[i]:
        turn = 0
        x = li[i]
        x_index = i
        sum_x = temp[x_index][0] + sum_x
        print("XXXX")
        print(i,sum_x)
    else:
        turn = 1
        y = li[i]
        y_index = i
        sum_y = temp[y_index][1] + sum_y
        print("YYYY")
        print(sum_y) 
        
print(sum_x, sum_y)
print(sum_x - sum_y)
 """




    
    
