# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

t=int(input())

for _ in range(t):
    arr=list(input().split())
    n=int(arr[0])
    string=arr[1]

    ans=""
    for i in range(len(string)):
        for j in range(n):
            ans+=string[i]
    print(ans)