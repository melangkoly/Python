# 글로벌 변수
global_a = 1
global_b = "Global Scope"

# 사용자 정의 함수
def func():
    # 로컬 변수 선언
    local_a = 2
    local_b = "Local Scope"

    # 로컬 심볼 테이블 확인
    print(locals())



# 심볼 테이블 확인
def symbol_table():
    # 글로벌 심볼 테이블 확인
    print(globals())
    print(type(globals()))

    # 심볼테이블은 객체의 심볼, 객체의 ID 를 담고 있는 사전
    print("global_a :", globals().get("global_a"))
    print("global_b : ", globals().get("global_b"))

    func()

    # 객체 내부의 __dict__ 속성을 확인하면 객체 내부의 심볼 테이블 확인 가능
    # 1. 정의된 함수 객체 내부의 심볼 테이블 확인
    func().dynamic = "Hello"
    print(func().__dict__)

    # 2. 객체 내부의 심볼 테이블 확인
    print(MyClass.__dict__) # 사용자 정의 클래스
    print(int.__dict__) # 내장 클래스의 심볼 테이블

def ref_count():
    """
    참조 카운트 객체
    """
    x = object()
    print(x, type(x))

    # 참조 카운트 확인
    import sys # 시스템 모듈 임포트
    print("REFCOUNT:", sys.getrefcount(x))

    y = x # y에 x의 참조 주소를 복사
    print("REFCOUNT:", sys.getrefcount(y))

    # x의 참조 삭제
    del x
    print("REFCOUNT:", sys.getrefcount(y))

    # 참조 카운트가 0인 객체 발견 시 처리해버림

def object_id():
    """
    객체 ID에 관한 예제 : 객체 ID 는 겍치의 참조 주소
    """

    # 불변 자료형 : 값이 같으면 동일 객체
    i1 = 10
    i2 = int(10)
    print("int : ", hex(id(i1)), hex(id(i2)))

    # 가변 자료형 : 값이 같아도 별개의 객체
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]

    print("List:", hex(id(lst1)), hex(id(lst2)))

    lst3 = lst2  # 참조 복사 : 객체 주소의 복사
    print("참조 복사 :", hex(id(lst2)), hex(id(lst3)))

    # == : 동등성의 비교 (값이 같은가), is 는 동일성의 비교 ( 주소가 같은가)
    print("불변 객체의 비교 : ", i1 == i2, i1 is i2)
    print("가변 객체의 비교 : ", lst1 == lst2, lst1 is lst2)

def object_copy():
    """
    객체의 복제
    """
    import  copy

    # 레퍼런스 복사 : 객체의 주소값만 복사 -> 같은 객체
    a = 1
    b = a
    print("a is b ? ", a is b)

    # 얕은 복제
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]
    print("a :", a)
    print("b :", b)
    print("x :", x)
    y = x

    print("x is y ?", x is y) # 같은 객체다
    x[0][2] = 10
    print("x :",x)
    print("y:", y)

    y = copy.copy(x)
    print("얕은 복제 :",  x is y) # 다른 객체다
    print("x :", x)
    print("y:", y)
    x[0][2] = 3
    print("x :", x)
    print("y:", y)
    # 객체 자체는 별개의 객체로 복제 됬지만
    # 내부 데이터는 여전히 동일 객체다
    print("x[0] is y[0] ? ", x[0] is y[0])

    # deepcopy (깊은 복제)
    # 가장 하위의 요소로부터 새 객체를 주기적으로 만들어서 객체를 재구성
    y = copy.deepcopy(x)
    print("x is y ? ", x is y)
    print("x[0] is y[0] ?", x[0] is y[0])
    print("x[1] is y[1] ? ", x[1] is y[1])
    x[0][2] = 20
    print("x:", x)
    print("y:", y)


if __name__ == "__main__":
    #symbol_table()
    #ref_count()
    #object_id()
    object_copy()