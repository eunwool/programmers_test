# # 숫자의 표현
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12924'
# def solution(n):
#     result = 0
#     for i in range(1, n + 1):
#         a = 0
#         while True:
#             a += i
#             i += 1
#             if a > n: break
#             if a == n: result += 1
#     return result

# # 영어 끝말잇기
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12981'
# def solution(n, words):
#     pass

# n = 3
# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# print(solution(n, words))

# # 다음 큰 숫자
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12911'
# def solution(n):
#     a = bin(n)[2:].count('1') ; result = 0
#     while True:
#         n += 1
#         if a == bin(n)[2:].count('1'): result = n ; break
#     return result

# # 124 나라의 숫자
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12899'
# def solution(n):
#     rev_base = '' ; result = ''
#     while n > 0:
#         n, mod = divmod(n, 3)
#         rev_base += str(mod)
#     print(rev_base)
#     rev_base = rev_base[::-1]

#     for i in rev_base:
#         if i == '0': result += '1'
#         if i == '1': result += '2'
#         if i == '2': result += '4'
#     return result
    

# n = 3
# print(solution(n))

# # 줄 서는 방법
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12936'
# def solution(n, k):
#     n = [i for i in range(1, n + 1)]
# n = 3 ; k = 5
# print(solution(n, k))

# # 문자열 압축
# 'https://school.programmers.co.kr/learn/courses/30/lessons/60057'
# def solution(s):
#     pass
# s = "aabbaccc"
# print(solution(s))

# # 행렬의 곱셈
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12949'
# def solution(arr1, arr2):
#     return arr1 * arr2

# arr1 = [[1, 4], [3, 2], [4, 1]]
# arr2 = [[3, 3], [3, 3]]
# print(solution(arr1, arr2))

# # 가장 큰 수
# 'https://school.programmers.co.kr/learn/courses/30/lessons/42746'
# def solution(numbers):
#     arr = [] ; count_arr = [] ; result = '' ; a= len(numbers)
#     arr1 = [0 for i in range(a)]
#     for i in numbers:
#         if i < 10: arr.append([i, 0])
#         if 10 <= i and i < 100: arr.append([i / 10, 1])
#         if 100 <= i and i < 1000: arr.append([i / 100, 2])
#     for i in range(len(arr)):
#         count = len(arr) - 1
#         for j in range(len(arr)):
#             if i != j:
#                 if arr[i][0] > arr[j][0]: count -= 1
#                 elif arr[i][0] == arr[j][0]:
#                     if arr[i][1] < arr[j][1]: count -= 1
#         count_arr.append(count)
#     count = 0
#     print(count_arr)
#     for i in count_arr:
#         arr1[i] = numbers[count]
#         count += 1
#     for i in arr1:
#         result += str(i)
#     return result


# numbers = [3, 30, 34, 5, 9]
# print(solution(numbers))

# # 수식 최대화 [카카오 인턴]
# 'https://school.programmers.co.kr/learn/courses/30/lessons/67257'
# def solution(expression):
#     count = 0 ; arr = [] ; count_num = [] ; num = '' ; a = []
#     for i in range(len(expression)):
#         if expression[i] in ['+', '-', '*']:
#             arr.append(expression[i])
#             count_num.append(num)
#             num = ''
#         else: num += expression[i]

#         if i == len(expression) - 1: count_num.append(num)
#     print(arr)
#     while True:
#         if '*' in arr:
#             if arr[count] == '*':
#                 a.append(int(count_num[count]) * int(count_num[count + 1]))
#                 arr[count] = 0
#                 count += 2
#             else: a.append(int(count_num[count])) ; count += 1
#         else: a.append(int(count_num[count])) ; count += 1

#         if count == 5: break
#     print(a)
#     while True:
#         if 0 in arr:
#             arr.remove(0)
#         else: break

#     b = a.index(max(a))
#     if b != 0:
#         if arr[b - 1] == arr[b]: c = 0
#         else: c = 1
#     else:
#         if arr[b] == '+': c = 0
#         else: c = 1
    
#     print(arr)
#     print(b)
# expression = '100-200*300-500+20'
# print(solution(expression))

# # 최솟값 만들기
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12941'
# def solution(A, B):
#     A.sort() 
#     B.sort()
#     result = 0
#     for i in range(len(A)):
#         result += (A[i] * B[len(A)- 1 - i])
#     return result

# # 문자열 압축
# 'https://school.programmers.co.kr/learn/courses/30/lessons/60057'
# def solution(s):
#     count = 0 ; n = 2 ; a = ''
#     while True:
        

# s = 'aabbaccc'
# print(solution(s))

# # 최댓값과 최솟값
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12939'
# def solution(s):
#     return str(min([int(i) for i in s.split(' ')])) + ' ' + str(max([int(i) for i in s.split(' ')]))

# # JadenCase 문자열 만들기
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12951'
# def solution(s):
#     a = 0 ; result = ''
#     for i in s:
#         if a == 0:
#             if i.isalpha(): result += i.upper() ; a += 1
#             else: result += i ; a += 1
#         else: result += i.lower()

#         if i == ' ': a = 0
#     return result

# # 짝지어 제거하기
# 'https://school.programmers.co.kr/learn/courses/30/lessons/12973'
# def solution(s):
#     s = list(s)
#     count = 0 ; a = 0 ; b = '' ; c = []
#     if len(s) % 2 == 1: return 0
#     else:
#         while a < (len(s) / 2):
#             count = 0 ; b = '' ; c = 0
#             while count < len(s):
#                 if b == s[count]:
#                     c.append(count)
#                     break
#                 else: b = s[count]    
#                 count += 1
#             print(s)
#             if c != 0:
#                 del s[c - 1]
#                 del s[c - 1]
#             a += 1
            
#         if len(s) != 0: return 0
#         else: return 1
# s = 'cdcd'
# print(solution(s))

# 주차 요금 계산
#'https://school.programmers.co.kr/learn/courses/30/lessons/92341'
def solution(fees, records):
    report = [] ; result = [] ; result_fee = []
    for i in records:
        time = (int(i[0:2]) * 60) + int(i[3:5])
        car_number = i[6:11]
        count = 0 ; time_a = 0 ; fee = 0 ; a = 0
        for j in report:
            if j[1] == car_number: count += 1 ; time_a = j[0]
        if count == 0: report.append([time, car_number])
        else: 
            fee += (time - time_a)
            report.remove([time_a, car_number])        
            for i in result:
                if i[1] == car_number: i[0] += fee ; a = 1
            if a == 0: result.append([fee, car_number])
    if len(report) != 0:
        for i in report:
            fee = 1440 - i[0]
            car_number = i[1]
            for j in result:
                if j[1] == car_number: j[0] += fee
    result.sort(key=lambda x:x[1])
    for i in result:
        count = 0
        if i[0] > fees[0]: 
            count += fees[1]
            count += ((1440 - i[0]) / fees[2]) * fees[3] 
        else: count = fees[1]
        result_fee.append(count)
    return result_fee


        
            
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
 "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))