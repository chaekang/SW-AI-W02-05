## 0부터 n까지의 합
# 방법 1
def nsum(n):
    result=0
    for i in range(n+1):
        result+=i
    return result

# 방법 2
def nsum(n):
    return sum([i for i in range(n+1)])

# 방법 3
def nsum(n):
    return sum(list(range(n+1)))

## 거듭제곱
def exp(b, n):
    if (n==0):
        return 1
    return b * exp(b, n-1)

def fast_exp(b, n):
    if (n == 0):
        return 1
    if (n % 2 == 0):
        return fast_exp(b, n/2) * fast_exp(b, n/2)
    else:
        return b * fast_exp(b, n-1)

# 피보나치 수열(tree recursion)   
def fib(n):
    if (n<=1):
        return n
    return fib(n-1)+fib(n-2)

# 거스름돈
def change(coins, k):
    if k==0:
        return 1
    if k<0 or len(coins)==0:
        return 0
    return change(coins[1:], k)+change(coins, k-coins[0])

# 하노이탑
def hanoi(n, fr, mid, to):
    if (n==1):
        print (str(fr)+" "+str(to))
        return
    
    hanoi(n-1, fr, to, mid)
    print(str(fr)+" "+str(to))
    hanoi(n-1, mid, fr, to)

hanoi(6, 1, 2, 3)