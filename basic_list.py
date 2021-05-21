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

    # 다양한 기초 산술 함수 제공
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("SUM : ", sum(lst))
    print("MIN : ", min(lst))
    print("MAX : ", max(lst))
    print("AVG : ", sum(lst) / len(lst))

def list_method():
    """
    리스트의 메소드들
    """
    lst = [10, 2, 22, 9, 8, 33, 4, 12]
    print("원본 : ", lst)
    copy = lst.copy() # 복제 메소드
    # Reverse : 리스트의 반전
    copy.reverse()
    print("Reverse : ", copy)

    copy = lst.copy()
    print("원본 : ", copy)

    # Sorting
    # 메소드로서의 sort -> 내부 데이터를 변경
    # 문법으로서의 sort -> 데이터를 변경시키지 않고 정렬된 새 리스트를 반환

    result = sorted(copy) # copy를 정렬 -> 새 리스트로 변환
    print("SORTED ASC : " , result)
    result = sorted(copy, reverse = True) # 내림차순 정렬
    print("SORTED DESC : " , result)
    #   정렬 키 함수 정의
    # 정렬 키 함수를 전달 -> 정렬 기준을 변경
    print("원본 : ", copy)
    result = sorted(copy, key=str) # 키 함수를 str로 변경
    print("SORTED key=str :", result)

# 정렬 기준의 사용자 정의
# 리스트의 요소를 5로 나눈 나머지 역순으로 정렬
def key_func(val): # 사용자 정의 키 함수
    return val % 5
    result = sorted(copy, key=key_func(), reverse=True)

    print("SORTED key=custom DESC : ", result)

    # sorted 함수 -> 원본은 변경시키지 않음
    # sort 메소드 -> 원본 내부 데이터 변경
    copy.sort(key_func(), reverse=True)

def stack_ex():
    """
    리스트를 활용한 스택의 구현
        append and Pop 으로
    """
    stack = []
    # 입력
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("STACK :", stack)

    # 인출
    print("POP : ", stack.pop())
    print("POP : ", stack.pop())
    print("POP : ", stack.pop())
    if len(stack): # 스택이 비어있지 않으면 Pop 해라
        print("POP : ", stack.pop())
    else:
        print("스택이 비어있습니다")

def queue_ex():
    """
    리스트를 활용한 Queue의 구현
        Append And POP
    """
    queue = []
    queue.append(10)
    queue.append(20)
    queue.append(30)
    print("QUEUE :", queue)

    # 인출
    print(queue.pop(0)) # 0번 째 인덱스 인출
    print(queue.pop(0))
    print(queue.pop(0))

if __name__ == "__main__":
    #define_list()
    #list_oper()
   #list_method()
    #stack_ex()
    queue_ex()