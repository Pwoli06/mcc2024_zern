#Problem2

import sys
sys.stdout = open('c:/Code/Competitive Programming/mcc2024/output2.txt', 'w')
sys.stdin = open('c:/Code/Competitive Programming/mcc2024/input2.txt', 'r')

#n = no of guests, m = no of gifts
n, m = map(int, input().split())
li = list(map(int, input().split()))
sorted_list = sorted(li)
#print(li)
#print(sorted_list)

counter = 0 #the no that will be replace
sorted_counter = 0 #to count the no of same int
no = 1 #number to compare
store = 0
store = store + m
#print("")

for i in range(n):
    if li[i] < sorted_list[m]:
        li[i] = 1
        store = store - 1
    
    if li[i] >= sorted_list[m]:
        counter += 1

for i in range(n):
    if store!= 0:
        if li[i] == sorted_list[m]:
            li[i] = 1
            store = store - 1

for i in range(n):
    if li[i] != 1:
        li[i] = 0



print(*li)












# tier = 1
# counter = []
# z = 0


# for i in range(n):
#     for i in range(n):     
#         if li[i] == tier:
#             counter.append(li[i])
#         if len(counter) <= m:
#             z = len(counter)
#             li[i] = "1"           
#         print(counter)
#         print(z)
#     tier = tier + 1



# # remaining = m - z

# # for i in range(n):
# #     if sorted_list[i] != 1:
# #         li[i] == 1
# #         remaining -= 1

# # for i in range(n):
# #     if li[i] != 1:
# #         li[i] = 0
              
# # print(li)


         