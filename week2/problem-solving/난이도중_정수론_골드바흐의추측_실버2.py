# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

import sys
import math

t = int(sys.stdin.readline())

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    
    return True

for _ in range(t):
    n = int(sys.stdin.readline())

    a = n//2
    b = n//2

    while True:
        if (isPrime(a) and isPrime(b)):
            if (a + b == n):
                print(str(a) + " " + str(b))
                break
        a -= 1
        b += 1