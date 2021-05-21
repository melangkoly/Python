def define_tuple():
    """
    튜플 정의 연습
    """
    tp = tuple()
    print(tp, type(tp))

    # 캐스팅 : 다른 순차자료형으로 튜플 생성
    tp = tuple({1, 3, 5, 7, 9})
    print(tp, type(tp))

    tp = () # 빈 튜플
    tp2 = (1,) # 요소의 갯수가 1개일 때 마지막에 반드시 ,를 붙여줘야 함
    tp3 = (1, 2, 3)
    print(tp, tp2, tp3)

def tuple_oper():
    """
    튜플의 연산
        대부분 list와 비슷 leng, 인덱싱, 슬라이싱, In 사용 가능
        immutable 불변형
            슬라이싱을 이용한 치환은 불가
            메소드가 한정적
    """
    tp = (1, 2, 3, 4, 5)
    # 길이를 구할 수 있다
    print(tp, "Length : ", len(tp))
    # 인덱스 접근 가능
    print(tp[0], tp[1], tp[2], tp[3], tp[4])
    print(tp[-5], tp[-4], tp[-3], tp[-2], tp[-1])

    # tp[3] = 0 : 불변형이기에 에러 뜸

    # 연결, 반복, 포험여부 확인 등은 모두 리스트와 동일

def tuple_methods():
    # 메소드가 별로 없다
    tp = (10, 20, 10, 20)
    # 검색
    print("1st 20 : ", tp.index(20))
    print("2nd 20 : ", tp.index(20, 2)) # 검색범위의 제한

    # 갯수 확인
    print("COUNT of 20 : ", tp.count(10))

def packing_unpacking():
    """
    튜플의 패킹 & 언패킹
    """
    tp = (10, 20, 30, "Python")
    print(tp, type(tp))
    tp = 10, 20, 30, "Python" # 괄호로 명시하지 않아도 스스로 튜플로 인식함 이것을 Packing 이라 부름
    print(tp, type(tp))

    # 기본 Unpacking
    (a, b, c, d) = tp
    print(a, b, c, d)
    a, b, c, d = tp
    print(a, b, c, d)

    # 좌변의 갯수와 우변의 갯수가 일치하지 않으면 Value Error
   # a, b, c, d, e = tp

    # 확장 언패킹
    # 지정되지 않은 변수 앞에 *
    a, *b = tp
    print(a, b)

    *a, b = tp
    print(a, b)

    a, *b, c = tp
    print(a, b, c)


if __name__ == "__main__":
    #define_tuple()
    #tuple_oper()
    #tuple_methods()
    packing_unpacking()