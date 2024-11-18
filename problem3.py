#Problem3
import sys
sys.stdout = open('c:/Code/Competitive Programming/mcc2024/output3.txt', 'w')
sys.stdin = open('c:/Code/Competitive Programming/mcc2024/input3.txt', 'r')

total_test_case = int(input())
ans = 0
total = 0
x = 0 #iteration

for i in range(total_test_case):
    n = int(input())
    li = sorted(list(map(int, input().split())), reverse=True)
    #print("################")
    #print(li)


    for j in range(len(li)):
        #print(li[j+1])
        total = total *2
        total = (total+ li[j])
        total = total % (10**9+7)

        #print(total)
        #print(j)
    

    print(total)   
    total = 0


        
