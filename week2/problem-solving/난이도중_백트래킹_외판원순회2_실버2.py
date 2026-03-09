# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

n=int(input())

arr=[0]*n

for i in range(n):
    arr[i]= list(map(int, input().split()))

result=list()
def backtracking(x, y, cost, path):
    if (arr[x][y] == 0):
        return
    
    # if (cost == n):
        