# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948

from collections import deque

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    indegree = [0]*(n+1)
    graph = {i:[] for i in range(n+1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        indegree[v] += 1
        graph[u].append((v, w))

    han, rome = map(int, input().split())

    q = deque()
    
    max_time=0
    roads=0
    time = [0]*(n+1)

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        des, time = q.popleft()
        for i in range(len(graph[des])):
            indegree[graph[i]] -= 1
            