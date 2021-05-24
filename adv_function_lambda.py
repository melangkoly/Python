# Lambda 함수 : 이름이 없는 익명 함수
def square(x):
    return x ** 2

for i in range(10):  # 0 ~ 9
    print("{} : {}".format(i, square(i)), end= ' ')
else:
    print()

# Lambda 식으로 교체
for i in range(10):
    print("{} : {}".format(i, (lambda x : x ** 2)(i)), end= ' ') # 즉시 실행 람다 식
else:
    print()

# lambda 를 이용한 sort 키함수 정의
strings = "Life is too short, you need python".upper().replace(",", "").split()
print("Strings : ", strings)
# 문자열의 길이를 기준으로 정렬
def strlen(x):
    return len(x)

result = sorted(strings,key = lambda x: len(x), reverse=True)
print("Len DESC : ", result)
