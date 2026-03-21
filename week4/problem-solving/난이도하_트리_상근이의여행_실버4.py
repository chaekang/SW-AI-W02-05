# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n ,m = map(int, input().split())

        graph = {i:[] for i in range(1, n+1)}

        for i in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        print(n-1)