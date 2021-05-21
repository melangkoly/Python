def define_list():
    """
    리스트의 정의 연습
    """
    lst1 = list() # 빈리스트
    print(lst1, type(lst1) )
    lst2 = [] # []
    lst3 = [1, 2, "python"]
    print(lst2, lst3)
    lst4 = list("Python")
    print(lst4)

def list_oper():
    lst = [1, 2, "Python"]

    # 길이의 확인
    print(lst, "length", len(lst))
    #인덱싱
    print(lst[0], lst[1], lst[2]) # 정인덱싱
    print(lst[-3], lst[-2], lst[-1]) # 역인덱싱

    # 슬라이싱
    print(lst[1:3])
    print(lst[1:])
    print(lst[:3])
    print(lst[:])

    copy = lst[:]
    print(copy is list) # 복사본과 원본은 별개의 객체로 본다

    # 연결 ( 원본을 바꾸지 않고 단순히 두 리스트를 연결한 새 리스트를 반환
    print(lst + ["Java", True, 3.14159])
    print("원본 : ", lst)

    # append vs extend
    copy.append(["Java", True, 3.14159]) # 개별 요소 추가
    print(copy)
    copy.extend(["Java", True, 3.14159]) # 다른 리스트를 연결하여 원본을 확장 바꿈
    print("Extend : ", copy)

    # 인서트
    copy.insert(2, [1, 2, 3]) # 2 번째 인덱스 부터 삽입
    print("Insert : ", copy)

    # 반복 (*)
    print("원본 : ", lst)
    print("반복 : ", lst * 3)

    #  포함여부 확인
    print("Python" in lst) # lst에 Python이 포함?
    #   인덱스의 확인
    print("Index : ", lst.index("Python"))

    if "Java" in lst: # 방어구문 탑재
       print("INDEX : ", lst.index("Java")) # 없는 객체 검색시 ValueError

    print("COPY : ", copy)

    #   항목의 갯수
    print("COUNT : " , copy.count("Python"))

    # 삭제
    del copy[0] # copy 의 0번 인덱스 삭제
    print("DEL : ", copy)

    # 삭제 Remove
    copy.remove(3.14159)
    print("REMOVE : ", copy)

    # 슬라이싱을 이용한 치환
    # 메서드 이용보다 슬라이싱 이용 치환을 먼저 하세요
    lst =  [1, 2, 123, 1234, 12345]
    print("원본 : ", lst)
    lst[0 : 2] = [10, 20]
    print(lst)
    # 슬라이싱을 이용한 삭제
    lst[0 : 2] = [] # 슬라이싱 범위에 빈 리스트 할당
    print(lst)
    # 슬라이싱을 이용한 삽입
    lst[1 : 1] = ['inserted']
    print(lst)
    # 맨 마지막 삽입
    lst[4:] = ['appended']
    print(lst)
    # 맨 앞에 삽입
    lst[:0] = ['prepended']
    print(lst)

    # 다양한 기초 산술 함수 제공 ㅋ
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("SUM : ", sum(lst))
    print("MIN : ", min(lst))
    print("MAX : ", max(lst))
    print("AVG : ", sum(lst) / len(lst))



if __name__ == "__main__":
    #define_list()
    list_oper()