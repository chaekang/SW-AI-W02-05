# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

if __name__ == "__main__":
    n, m = map(int, input().split())

    dp=[0]*(n+1)
    for i in range(m):
        x = int(input())
        dp[x].append((-1,0))

    dp[1].append((0, 0))
    dx = [-1, 0, 1]

    for i in range(1, n):
        cnt, jump = dp[i]
        for j in range(3):
            nx = jump + dx[j]
            if (nx < 1):
                continue

            n_cnt = cnt+1
            n_jump = nx
            if (dp[i+nx][0] == -1):
                continue
            dp[i+nx].append((n_cnt, n_jump))