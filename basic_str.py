def define_str():
    # 한 줄 문자열의 정의
    s1 = "Helo Python"
    s2 = str("Hello Python")
    s3 = str(3.14159)

    print(s1, s2, s3)
    print(type(s1), type(s2), type(s3))

    print("s1 은 str의 객체 ", isinstance((s1, str)))

    #   여러 줄 문자열의 정의
    #   쌍다옴표 세 개 ("""), 홑따옴표 세 개(''')
    s4 = """Life is too short, you need python
    크크루삥뽕"""

    print(s4)

def String_oper():
    str1 = "Python"
    str2 = "Second String"

    # 길이
    print("str1 len", len(str1))

    # 변경 불가 자료형
    #str1[0] = 'f' -> error

    #인덱싱 : 배열과 비슷하게 인덱스로 접근 가능
    #인덱스의 범위 : 0 ~ len -1
    #print("정인덱싱 : ", str1[0], str1[1], str1[2], str[3], str1[4], str1[5])
    #print("역인뎅싱 : ", str1[-6], str[-5], str1[-4], str1[-3], str1[-2], str1[-1])


    print(str1[2 : 4])
    print(str1[-4 : -2])
    print(str1[0 : 3])
    print(str1[:3])
    print(str1[3 : len(str1)])
    print(str1[3 :])

if __name__ == "__main__":
    #define_str()
    String_oper();