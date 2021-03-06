# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def prime_number(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

x, y = map(int, input().split())

for i in range(x, y+1):
    if prime_number(i):
        print(i)