# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

if __name__ == "__main__":
    formula = input()

    tmp=0
    num=""
    isMinus=False
    ans=0
    for i in range(len(formula)):
        num += formula[i]
        if (formula[i] == "+" or formula[i] == "-" or i == len(formula)-1):
            if formula[i] == "+" or formula[i] == "-":
                num = num[:-1]
            
            tmp += int(num)
            num=""
            if (formula[i] == "-" or i == len(formula)-1):
                if (isMinus):
                    ans -= tmp
                    tmp=0

                else:
                    ans += tmp
                    tmp=0
                    isMinus=True
        
    print(ans)