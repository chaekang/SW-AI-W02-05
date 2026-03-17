# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 999999999999
    left = 0
    right = n-1

    x = 0
    y = 0

    while (left < right):
        if (abs(ans)>abs(arr[left]+arr[right])):
            x = arr[left]
            y = arr[right]
            ans = x + y

        if (arr[left]+arr[right] == 0):
            x = arr[left]
            y = arr[right]
            break
        elif (arr[left]+arr[right] < 0):
            left += 1
        else:
            right -= 1
    
    print(str(x) + " " + str(y))