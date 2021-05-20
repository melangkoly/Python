def arith_oper():
    print("====산술 연산")
    #+, -
    print(7/3)

    #정수 나눗셈 몫
    print(7//3)
    print(7 % 3)

    #divmod
    print(divmod(7, 3)) #7과 3을 나눈 값과 나머지
    print(divmod(7, 3)[0]) # 몫
    print(divmod(7, 3)[1]) # 나머지

    # 제곱 연산자
    print(7 ** 3) # 7의 3 승
    print(pow(7, 3)) # 내장 수치 제곱함수

def complex_ex():
    print("=======복소수")
    print(3 + 4j) # 실수부 + 허수부 j
    print(3 + 4j.real) # 실수부 반환
    print(3 + 4j.imag) # 허수부 반환
    print(3 + 4j.conjugate()) # 켤레 복소수

    print(complex_ex(3, 4)) # 타입 함수를 이용한 복소수 선언

def rel_oper():
    print("=======비교연산")
    print("1 > 3 ?", 1 > 3)
    print("1 < 3 ? ", 1 < 3)
    print("6 equals 9 ?", 6 == 9)
    print("6 not equals 9 ?", 6 != 9)

    s1 = "Python"
    s2 = "Python"

    print("문자열의 ==", s1 == s2)

    #   복합 관계식
    a = 6
    # a가 0보다 크고 10 보다 작은 값
    print(a > 0 and a < 10)
    print(0 < a and a < 10)
    print(0 < a < 10)

    # 수치형 이외 다른 타입 객체 비교
    print("문자열의 대소 : ", "abcd" > "abd")
    print("튜플의 대소:", (1, 2, 4) > (1, 3, 1))
    print("리스트의 대소:", [1, 2, 4] < [1, 3, 1])

    # 동질성의 비교 ==를 사용하고
    # 동일성의 비교는 비교 연산자들을 사용한다
    a = 10
    b = 20
    c = a
    print("a == b?", a == b)
    print("a is b?", a is b)
    print("a == c ?", a == c)

def variable_ex(): # 변수
    print("===== 변수")
    # 변수명은 문자, 숫자, _의 조합
    # 숫자로 시작 불가
    # 예약어도 사용 불가
    import keyword # keyword의 모듈 로드
    print(keyword.kwlist)
    print("키워드의 갯수 :", len(keyword.kwlist))

    # 유니코드 변수의 이름도 사용 가능 -> 권장치는 않음
    가격 = 12000
    print(가격 + 가격 * 0.1)

def assignment_ex(): #치환문
    print("-----치환문")

    #   여러변수를 한꺼번에 할당ㅇ
    a, b =35, 53 # 좌변의 변수의 갯수와 우변의 변수값의 갯수가 같아야 한다
    print(a, b)

    #   값의 교환
    a, b = b, a
    print(a, b)

    #   같은 값을 동시에 할당
    x = y = z = 100
    print(x, y, z)

    #   중요 : 동적 타이핑
    #   파이썬은 변수 선언이 없고 값이 할당 될 때 타입이 정해짐
    a = 1
    print(a, "is", type(a))
    a = "Hello"
    print(a, "is", type(a))

    # isinstance #판별할 값
    print("a는 str의 객체 ?", isinstance(a, str))

def logical_ex():
    print("======논리연산")
    #   논리곱 (and : 둘 다 True 일 때만 참)
    #   논리합 (or : 둘 중 하나면 참이면 참)
    #   논리 부정 (not : 참 < - > 거짓)
    a, b = 20, 30
    print(not a < b)
    print(a < b and a != b)
    print(a == b or a != b)


if __name__ == "__main__":
    #arith_oper()
    #complex_ex();
    #rel_oper()
    #variable_ex()
    #assignment_ex()
    logical_ex()