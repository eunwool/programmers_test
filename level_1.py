# 프로그래머스 연습문제 레벨1
# - 최대한 간단하게 풀어보기

# 직사각형 별찍기
'https://school.programmers.co.kr/learn/courses/30/lessons/12969'
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end = '')
    print(end = '\n')

# x만큼 간격이 있는 n개의 숫자
'https://school.programmers.co.kr/learn/courses/30/lessons/12954'
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

# 두 정수 사이의 합
'https://school.programmers.co.kr/learn/courses/30/lessons/12912'
def solution(a, b):
    if a > b:
        arr = [i for i in range(b, a + 1)]
    else:
        arr = [i for i in range(a, b + 1)]    
    return sum(arr)

# 나누어 떨어지는 숫자 배열
'https://school.programmers.co.kr/learn/courses/30/lessons/12910'
def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0: result.append(i)
    return sorted(result) if len(result) != 0 else [-1]

# 가운데 글자 가져오기
'https://school.programmers.co.kr/learn/courses/30/lessons/12903'
def solution(s):
    a = len(s)
    if a % 2 == 0:
        b = round(a / 2)
        return s[b - 1] + s[b]
    elif a % 2 == 1:
        return s[a // 2]

# 부족한 금액 계산하기
'https://school.programmers.co.kr/learn/courses/30/lessons/82612'
def solution(price, money, count):
    answer = [price * i for i in range(1, count + 1)]
    return 0 if money > sum(answer) else sum(answer) - money

# 나머지가 1이 되는 수 찾기
'https://school.programmers.co.kr/learn/courses/30/lessons/87389'
def solution(n):
    i = 1
    while True:
        if n % i == 1:
            break
        else : i += 1
    answer = i
    return answer

# 2016년
'https://school.programmers.co.kr/learn/courses/30/lessons/12901'
def solution(a, b):
    mon_data = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = 0
    for i in range(a - 1):
        day += mon_data[i]
    day += b
    # 1월 1일이 금요일
    day -= 4
    return days[day % 7]

# 두개 뽑아서 더하기
'https://school.programmers.co.kr/learn/courses/30/lessons/68644'
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = set(answer)
    answer = list(answer)
    return sorted(answer)

# 예산
'https://school.programmers.co.kr/learn/courses/30/lessons/12982'
def solution(d, budget):
    answer = 0 ; sum = 0
    d.sort()
    for i in d:
        if answer + i <= budget:
            answer += i
            sum += 1
    return sum

# 약수의 개수와 덧셈
'https://school.programmers.co.kr/learn/courses/30/lessons/77884'
def solution(left, right):
    a = [i for i in range(left, right + 1)]
    b = []
    answer = 0
    for i in a:
        for j in range(1, i + 1):
            if i % j == 0:
                b.append(j)

        if len(b) % 2 == 0:
            answer += i
        elif len(b) % 2 == 1:
            answer -= i        
        b = []
    return answer

# 모의고사
'https://school.programmers.co.kr/learn/courses/30/lessons/42840'
def solution(answers):
    user_1 = [1, 2, 3, 4, 5]
    user_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    user_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    if len(answers) > len(user_1):
        user_1 = user_1 * ((len(answers) // len(user_1)) + 1)
        user_1 = user_1[:len(answers)]
    if len(answers) > len(user_2):
        user_2 = user_2 * ((len(answers) // len(user_2)) + 1)
        user_2 = user_2[:len(answers)]
    if len(answers) > len(user_3):
        user_3 = user_3 * ((len(answers) // len(user_3)) + 1)
        user_3 = user_3[:len(answers)]
    
    a, b, c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == user_1[i]:
            a += 1
        if answers[i] == user_2[i]:
            b += 1
        if answers[i] == user_3[i]:
            c += 1

    max_num = max(a, b, c)
    arr = [i for i in (a, b, c)]
    result = []
    for i in range(len(arr)):
        if arr[i] == max_num:
            result.append(i+1)
    return result

# k번째수
'https://school.programmers.co.kr/learn/courses/30/lessons/42748'
def solution(array, commands):
    arr = [] ; arr1 = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        for j in range(a - 1, b):
            arr.append(array[j])
        arr.sort()
        print(arr)
        arr1.append(arr[c - 1])
        arr = []
    return arr1

# 내적
'https://school.programmers.co.kr/learn/courses/30/lessons/70128'
def solution(a, b):
    arr = []
    for i in range(len(a)):
        arr.append(a[i] * b[i])
    return sum(arr)

# 음양 더하기
'https://school.programmers.co.kr/learn/courses/30/lessons/76501'
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# 없는 숫자 더하기
'https://school.programmers.co.kr/learn/courses/30/lessons/86051'
def solution(numbers):
    answer = -1
    answer = answer + 1
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer

# 숫자 문자열과 영단어
'https://school.programmers.co.kr/learn/courses/30/lessons/81301'
def solution(s):
    change_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    s = list(s)
    result = ''
    arr = ''
    for i in s:
        if i.isdigit() == True:
            result = result + i
        elif i.isdigit() == False:
            arr += i
        if arr in change_num:
            result += str(change_num.index(arr))
            arr = ''
    return int(result)

# 최소직사각형
'https://school.programmers.co.kr/learn/courses/30/lessons/86491'
def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    a = [] ; tep = 0 ; tep1 = 0
    for i in sizes:
        if i[0] > tep: tep = i[0]
        if i[1] > tep1: tep1 = i[1]
    return tep * tep1

# 같은 숫자는 싫어
'https://school.programmers.co.kr/learn/courses/30/lessons/12906'
def solution(arr):
    a = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            a.append(arr[i])
    a.append(arr[len(arr)-1])
    return a

# 문자열 다루기 기본
'https://school.programmers.co.kr/learn/courses/30/lessons/12918'
def solution(s):
    s = list(s)
    a = True ; b = 0
    if len(s) == 4 or len(s) == 6:
        if s[b] == '-':
            b += 1
        else:
            while a:
                if s[b].isdigit() == True:
                    b += 1
                else: a = False

                if b == len(s) : break
        return a
    else: return False

# 시저 암호
'https://school.programmers.co.kr/learn/courses/30/lessons/12926'
def solution(s, n):
    s = list(s) ; result = ''
    for i in s:
        if i.isalpha() == True:
            if ord(i) <= 90:
                if ord(i) + n > 90:
                    result += chr(ord(i) + n - 26)
                else: result += chr(ord(i) + n)
            elif ord(i) > 90:
                if ord(i) + n > 122:
                    result += chr(ord(i) + n - 26)
                else: result += chr(ord(i) + n)
        else: result += i
    return result

# 3진법 뒤집기
'https://school.programmers.co.kr/learn/courses/30/lessons/68935'
def solution(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    return int(rev_base, 3)

# 소수 찾기
'https://school.programmers.co.kr/learn/courses/30/lessons/12921'
def solution(n):
    sieve = [True]*(n+1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    x = [i for i in range(2, n+1) if sieve[i] == True]
    answer = len(x)
    return answer

# 성격 유형 검사하기
'https://school.programmers.co.kr/learn/courses/30/lessons/118666'
def solution(survey, choices):
    answer = ''
    dicts = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)) : 
        if choices[i] - 4 < 0: # choices 값이 4 미만일 시, survey의 앞의 값 출력
            dicts[survey[i][0]] += 4 - choices[i]
        elif choices[i] - 4 > 0: # choices 값이 4 초과 시, survey의 앞의 값 출력
            dicts[survey[i][1]] += choices[i] - 4
    answer += 'T' if dicts['T'] >= dicts['R'] else 'R'
    answer += 'C' if dicts['C'] >= dicts['F'] else 'F'
    answer += 'J' if dicts['J'] >= dicts['M'] else 'M'
    answer += 'A' if dicts['A'] >= dicts['N'] else 'N'
    return answer
survey = ['AN', "CF", 'MJ', 'RT', 'NA']
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))

# 문자열 내 마음대로 정렬하기
'https://school.programmers.co.kr/learn/courses/30/lessons/12915'
def solution(strings, n):
    arr = [] ; arr_index = [] ; a = 0
    result = [0 for i in range(len(strings))]
    for i in strings:
        arr.append(ord(i[n]))
    for i in arr:
        for j in range(len(arr)):
            if i > arr[j]:
                a += 1
        arr_index.append(a)
        a = 0
    for i in range(len(strings)):
        result[arr_index[i]] = strings[i]
    return result 
    
    
        
    


strings = ['abce', 'abcd', 'cdx']
n = 2
print(solution(strings, n))