# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

from collections import deque

def bfs(graph, start, visited):
    global n
    q = deque()

    q.append(start)
    visited[start] = True

    ans = [0] * (n+1)

    while q:
        x = q.pop()
        
        for i in range(len(graph[x])):
            tmp = graph[x][i]
            if visited[tmp]:
                continue

            visited[tmp]=True
            q.append(tmp)
            ans[tmp] = x

    return ans

if __name__ == "__main__":
    n = int(input())

    graph = {i:[] for i in range(n+1)}
    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n+1)
    ans = bfs(graph, 1, visited)

    for i in range(2, n+1):
        print(ans[i])