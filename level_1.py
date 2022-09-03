# 프로그래머스 연습문제 레벨1
# - 최대한 간단하게 풀어보기

# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end = '')
    print(end = '\n')

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [x * i for i in range(1, n + 1)]

# 행렬의 덧셈
'https://school.programmers.co.kr/learn/courses/30/lessons/12950'
def solution(arr1, arr2):
    result = []
    a = len(arr1)
    for i in range(a):
        array = []
        for j in range(a):
            c = arr1[i][j] + arr2[i][j]
            array.append(c)   
        result.append(array)
    return result

# 핸드폰 번호 가리기
'https://school.programmers.co.kr/learn/courses/30/lessons/12948'
def solution(phone_number):
    a = len(phone_number)
    b = phone_number[a-4:]
    return ('*' * (a - 4)) + b

# 하샤드 수
'https://school.programmers.co.kr/learn/courses/30/lessons/12947'
def solution(n):
    a = list(map(int, str(n)))
    return True if n % sum(a) == 0 else False

# 평균 구하기
'https://school.programmers.co.kr/learn/courses/30/lessons/12944'
def solution(arr):
    return sum(arr) / len(arr)

# 콜라츠 추측
'https://school.programmers.co.kr/learn/courses/30/lessons/12943'
