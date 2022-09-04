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
def solution(n):
    count = 0
    if n != 1:
        while True:
            count += 1
            if n % 2 == 0: n = n / 2
            else: n = (n * 3) + 1

            if n == 1: break
            if count == 500: count = -1 ; break
    else: count = -1        
    return count

# 짝수와 홀수
'https://school.programmers.co.kr/learn/courses/30/lessons/12937'
def solution(num):
    return 'Even' if num % 2 == 0 else  'Odd'

# 제일 작은 수 제거하기
'https://school.programmers.co.kr/learn/courses/30/lessons/12935'
def solution(arr):
    if len(arr) > 1: arr.remove(min(arr)) ; return arr
    else: return [-1]

# 정수 제곱근 판별
'https://school.programmers.co.kr/learn/courses/30/lessons/12934'
def solution(n):
    if (n ** (1/2)) - round(n ** (1/2)) == 0:
        return ((n ** (1/2)) + 1) * ((n ** (1/2)) + 1)
    else : return -1

# 정수 내림차순으로 배치하기
'https://school.programmers.co.kr/learn/courses/30/lessons/12933'
def solution(n):
    a = list(map(str, str(n)))
    a.sort(reverse = True)
    return int(''.join(a))

# 자연수 뒤집어 배열로 만들기
'https://school.programmers.co.kr/learn/courses/30/lessons/12932'
def solution(n):
    a = list(map(int, str(n)))
    a.reverse()
    return a

# 자릿수 더하기
'https://school.programmers.co.kr/learn/courses/30/lessons/12931'
def solution(n):
    return sum(list(map(int, str(n))))

# 이상한 문자 만들기
'https://school.programmers.co.kr/learn/courses/30/lessons/12930'
def solution(s):
    s = list(s)
    b = 0 ; result = ''
    print(s)
    for i in s:
        if i == ' ':
            result += i
            b = 0
        else:
            if b == 0:
                result += i.upper()
                b += 1
            else:
                if b % 2 == 1:
                    result += i.lower()
                    b += 1
                elif b % 2 == 0:
                    result += i.upper()
                    b += 1
    return result

# 약수의 합
'https://school.programmers.co.kr/learn/courses/30/lessons/12928'
def solution(n):
    aa = []
    for i in range(1, n + 1):
        if n % i == 0: aa.append(i)
    return sum(aa)

# 문자열을 정수로 바꾸기
'https://school.programmers.co.kr/learn/courses/30/lessons/12925'
def solution(s):
    return int(s)

# 수박수박수박수박수박수
'https://school.programmers.co.kr/learn/courses/30/lessons/12922'
def solution(n):
    a = '수박'
    return a * int(n / 2) if n % 2 == 0 else a * int(n // 2) + '수'

# 서울에서 김서방 찾기
'https://school.programmers.co.kr/learn/courses/30/lessons/12919'
def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'

# 문자열 내림차순으로 배치하기
'https://school.programmers.co.kr/learn/courses/30/lessons/12917'
def solution(s):
    return (''.join(sorted(s)[::-1]))

# 문자열 내 p와 y의 개수
'https://school.programmers.co.kr/learn/courses/30/lessons/12916'
def solution(s):
    a = 0 ; result = True
    for i in s:
        if i =='p' or i =='P':
            a += 1
        elif i == 'y' or i == 'Y':
            a -= 1
    if a != 0: result = False
    return result