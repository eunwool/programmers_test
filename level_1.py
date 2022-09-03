# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end = '')
    print(end = '\n')

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [x * i for i in range(1, n + 1)]
2