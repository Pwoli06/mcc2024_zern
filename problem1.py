#Problem1

import sys
sys.stdout = open('c:/Code/Competitive Programming/mcc2024/output1.txt', 'w')
sys.stdin = open('c:/Code/Competitive Programming/mcc2024/input1.txt', 'r')

t = int(input())

for i in range(t):
    n, m, A, B= map(int, input().split())
    
    if A == n and B <= m:
        print("YES")
    elif B == n and A <= m:
        print("YES")
    elif A == m and B <= n:
        print("YES")
    elif B == m and A <= n:
        print("YES")
    else:
        print("NO")



    
    