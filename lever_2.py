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
def solution(numbers):
    arr = [] ; count_arr = [] ; result = ''
    for i in numbers:
        if i < 10: arr.append(i)
        if 10 <= i and i < 100: arr.append(i / 10)
        if 100 <= i and i < 1000: arr.append(i / 100)
    for i in arr:
        count = len(arr) - 1
        for j in arr:
            if i != j:
                if i > j: count -= 1
        count_arr.append(count)
    print(count_arr)
    for i in count_arr:
        result += str(numbers[i])
    return result


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))