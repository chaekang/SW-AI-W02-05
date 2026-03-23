# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

def dfs(graph, start, color, visited):
    visited[start] = color
    
    for i in range(len(graph[start])):
        cur = graph[start][i]

        if visited[cur] == -1:
            if dfs(graph, cur, 1-color, visited):
                return False
        elif visited[cur] == color:
            return False
        
    return True

if __name__ == "__main__":
    k = int(input())

    v, e = map(int, input().split())