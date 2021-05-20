def bool_ex():
    print("-----bool 연습")
    # 참 , 거짓
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판단
    # bool의 판정 방법
    print(bool(0), bool(1))
    a = 1
    print(a > 10) # 논리 연산 or 비교 연산의 결과

    b = a = 1
    print(b + 10)

    # bool은 bool의 객체 인가?
    print(isinstance(True, bool)) # True is Boolean?
    print(isinstance(True, int)) # True is Integer?

    # bool 캐스팅
    print("정수형", bool(10), bool(0))
    print("실수형", bool(3.14), bool(0.0))
    print("문자열", bool("Python"), bool(""))
    print("순차형", bool(1, 2, 3), bool([]))
    print("Map", bool({"a", 2}), bool({}))
    print("None", bool(None)) # None : Java의 null과 비슷

    # Circuit Break
    print("CB or 1 : ", [1, 2, 3] or []) #or 는 먼저 나온 True를 객체로 선택
    print("CB or 2 : ", [] or [1, 2, 3])
    print("CB and 1 : ", [1, 2, 3] and [4, 5, 6]) # and의 경우 논리식이 참이면 뒤쪽 객체를 선택
    print("CB and 2 :", [1, 2, 3] and []) # and 의 경우 전체 논리값이 false면 None 출력

def integer_ex():
    print("========정수형 연습")
    a = 23
    b = int(23)
    print(a, "is", type(a))
    print(b, "는 int의 객체?", isinstance(b, int))

    #   2진, 8진, 16진수 표현 가능
    b = 0b1101
    o = 0o23
    x = 0xFF

    print(b, o, x)

    # 3.x 대에서는 int와 long을 구분짓지 않는다
    #   long형의 저장크기인 64비트를 초과하는 정수조차 입력가능 ㄷㄷ
    i = 2 ** 2048
    print(i)
    print(i.bit_length()) # i 객체의 비트 수를 확인해라

    #   진법 변환 함수
    print(bin(2021))
    print(oct(2021))
    print(hex(2021))

def float_ex():
    # 실수형은 모두 float 형으로 표기
    print("========실수형 연습")
    a = 3.14159
    print(a, "is", type(a))
    b = float(3.0)
    print(b , "는 float의 객체인가", isinstance(b, float))
    #is_integer : 타입 판별이 아니라 값의 형태가 정수형(소숫점 아래 값이 없는형) 인지 확인
    print(a.is_integer() , b.is_integer())

    #   소수점 포함, e, E 지수 형태로 표현 가능
    c = 3e3 # 3 * 10 ** 3 == 3000.0
    d = -2E-5 # -2 * 10 ** -5 == -0.00002

    print(c, d)
    print(-2E-5 == -0.00002)

def complex_ex():
    print("======복소수 연습")
    # 복소수 : 실수부 + 허수부j
    a = 4 + 5j
    print(a, "is", type(a))

    b =  7 - 2j #실수부 7 허수부 -2
    print(b, "complex의 객체?", isinstance(b, complex))

    # 복소수 -> 수치형 -> 산술 연산 가능
    print(a + b)
    print(a, "의 실수부?", a.real)
    print(a, "의 허수부?", a.imag)
    print(a, "의 켤레복소수?", a.conjugate())

    # 타입 함수를 이용한 복소수의 생성
    c = 7
    d = 3
    e = complex(7, 3) #실수부 7, 허수부 3인 복소수 생성
    print(e, "is", type(e))

def builtin_math_function():
    print(abs(-1))
    print(int(3.14157))
    print(float(3))
    print(complex(1))
    print(divmod(5, 3))
    print(pow(2, 10))

def bit_oper(): # 비트 연산자 : int 데이터를 비트 단위로 정밀하게 제어
    print("========비트 연산자")
    # 비트 NOT : 1 <-> 0
    print(bin(5), bin(~5))

    # 비트 시프트 : << 좌측으로 이동 , >> 우측으로 이동
    bits =1
    print(bin(bits))
    bits = bits << 4 # 왼쪽으로 4비트 이동
    print(bin(bits))

    bits = 0b10101010
    print(bin(bits))
    print(bin(bits & 0b10)) # bit and
    print(bin(bits | 0b1111)) #bit or

if __name__ == "__main__":
    #integer_ex()
    #float_ex()
    #complex_ex()
    #builtin_math_function()
    bit_oper()