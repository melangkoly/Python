numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # 전체 집합
evens = {0, 2, 4, 6, 8} # 짝수 집합
odds = {1, 3, 5, 7, 9} # 홀수
mthree = {0, 3, 6, 9} # 3의 배수

def define_set():
    """
    SET 정의 연습
        set()
        {}
    """
    empty = set() # 빈 셋트
    print(empty, type(empty))
    empty = {} # 빈 사전
    print(empty, type(empty))

    # 특성상 순서가 없고 인덱스도 없고 슬라이싱도 안된다
    # 길이(파라미터의 수), 포함 여부 (in and not in)은 사용 가능
    print(numbers, "LENGTH : " , len(numbers))
    print("포함 여부 : ", 2 in numbers, 2 in evens, 2 in odds)

    # 캐스팅 : 다른 순차형으로 Set 만들기
    s = "Python Programming" # 문자열 안 쪽에 몇 개의 알파벳이 사용되었는가?
    chars = set(s.upper())
    print(s, chars)

    #  특성상 중복 허용 안함
    # list 의 중복값 제거에 유용함
    lst  = "Python Programming Java Programming".upper().split()
    print(lst)
    words = set(lst)
    print(words, len(words))

def set_methods():
    print("전체 집합 : ", numbers)

    # 파라미터 추가
    numbers.add(10) # 10 parameter를 추가함
    print(numbers)
    evens.add(10)
    print(evens)
    evens.add(4)
    print(evens) # 이미 있는 값을 추가해봤자 추가되지 않는다 'ㅅ';
    # 삭제 : discard , remove
    evens.discard(4)
    print(evens)
    evens.discard(4) # 없는 요소를 삭제해도 에러가 발생하지 않는다
    #evens.remove(4) # 요 놈은 없는 요소를 삭제하면 Key Error 발생!

    evens.update({2, 4, 6}) # 이미 2와 6은 있으니 삭제됬던 4만 추가됨
    print(evens)

def set_oper():
    """
    집합 연산
        교집합, 합집합, 차집합
    판별 연산
        모집합 여부, 부분 집합 여부
    """

    # 짝수 집합 합집합 홀수 집합 = 전체 집합
    print("짝수 합집합 홀수 : ", evens.union(odds) == numbers)
    print("짝수 합집합 홀수 : ", evens | odds == numbers)

    # 모집합, 부분 집합 판별
    print("전체 집합이 짝수 집합의 모집합? :", numbers.issuperset(evens))
    print("홀수 집합이 전체집합의 부분 집합? :", odds.issubset(numbers))

    #   교집합
    print("짝집 교집 3의 배수 : ", evens.intersection(mthree))
    print(mthree & odds == {3, 9})

    # 차집합
    print("전체 집합 차집합 짝수 집합 : ", numbers.difference(evens))
    print("전체 집합 차집합 짝수 집합 -> 홀수 집합? ", numbers - evens == odds )
if __name__ == "__main__":
    #define_set()
    #set_methods()
    set_oper()