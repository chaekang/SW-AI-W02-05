# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

from collections import deque

if __name__ == "__main__":
    n = int(input())

    time = [0] * (n+1)
    indegree  = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    ans = [0]*(n+1)

    for i in range(1, n+1):
        tmp = list(map(int, input().split()))
        time[i] = tmp[0]
        for j in range(tmp[1]):
            graph[tmp[j+2]].append(i)
            indegree[i]+=1

    q = deque()
    for i in range(1, n+1):
        if (indegree[i] == 0):
            q.append(i)
            ans[i]=time[i]

    while q:
        x = q.popleft()
        for i in graph[x]:
            ans[i] = max(ans[i], ans[x]+time[i])
            indegree[i]-=1
            if (indegree[i] == 0):
                q.append(i)
        
    print(max(ans))