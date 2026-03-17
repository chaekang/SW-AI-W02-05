# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

def turn(direction):
    global dir
    if (direction == "L"):
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    arr = [[0] * (n+1) for i in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    l = int(input())
    command = dict()
    for _ in range(l):
        x, c = input().split()
        command[int(x)] = c

    cnt = 0
    snake = deque([(1, 1)])
    x = 1
    y = 1

    dir = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while True:
        x += dx[dir]
        y += dy[dir]
        cnt+=1

        if (x<=0 or y<=0 or x>n or y>n):
            break

        if ((x, y) in snake):
            break

        if (arr[x][y] == 0):
            snake.popleft()
        else:
            arr[x][y] = 0

        snake.append((x,y))

        if (cnt in command):
            turn(command[cnt])

    print(cnt)