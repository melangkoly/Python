class MyString(str): # str 클래스를 상속받은 MyString
    pass # MyString은 str 클래스에서 모든 멤버들을 물려받는다
s = MyString() # 인스턴스 생성
print(type(s))
print(MyString.__bases__) # 기반 클래스 확인
print(str.__bases__) # 모든 클래스의 최상위 클래스는 Object 다

# 파이썬은 다중 상속이 가능하다 자바는 불가능
class myobj:
    pass

class chimera(str, myobj):
    pass

print(type(chimera))
print(chimera.__bases__)

# 하위 클래스 또는 파생 클래스 : issubclass 함수
print("Chimera는 str의 서브 클래스? ", issubclass(chimera, str))
print("Chemera는 myobj의 서브 클래스? ", issubclass(chimera, myobj))

# 상위 클래스 or 기반 클래스 : 별도 함수 없음 __bases__ 사용
# MyString은 str을 상속 -> str 의 모든 멤버를 상속

ms = MyString("Python")
print(ms)
print(dir(ms))
# str의 모든 메서드 활용
print(ms.upper())

# 클래스 생성
