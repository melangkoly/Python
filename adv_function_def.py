def dummy():
    pass

def my_function():
    print("Hello") # 끝날 때까지 함수 종료 선언이 필요 없을 때 return 생략 가능

def times(a, b): # 입력은 인수로 전달
    return a * b # 반환할 값이 있을 경우 return으로 반환


def none():
    return  # 반환 없이 return문만 사용하면 none이 반환

dummy()
print(dummy()) # None -> return 없음
print(times(10, 20))
print(none())

# 기본적으로 return 은 하나의 객체 반환
def max_value(a, b):
    if a > 0:
        return a
    else:
        return b
print(max_value(10, 20))

# return 문으로 여러 객체를 반환할 수 있다 -> 튜플로 패킹되어서 반환

def swap(a, b):
    return b, a # Tuple로 패킹된다

print(swap(10, 20), type(swap(10, 20)))

c, d = swap(10, 20)
print(c, d)