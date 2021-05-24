def hadling_exception():
    """
    예외 처리하기
    """
    lst = []

    try:
        lst[3] = 1
        4 / 0
        int("String")
    except:
        print("Error")

    # 예외 회피는 가능하지만 실제 무슨 오류인지 사실 확인이 불가능
    try:
        #lst[3] = 1
        #4 / 0
        int(12345667)
    except ValueError as e:
        print("정수로 변환 불가!")
        print(e, type(e))
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없다!")
        print(e, type(e))
    except IndexError as e: # 구체적인 예외 처리가 가능
        print("인덱스에 접근할 수 없다")
    except Exception as e: # 예외 객체의 심볼을 붙이면 어떤 예외인지 확인 가능
        print("Error")
        print(type(e))
    else: # try 블록에서 예외가 없을 때 한 번 실행
        print("예외 없음!")
    finally: # 예외 유무 관계 없이 항상 마지막에 -> 주로 자원 정리에 사용
        print("예외 처리 종료!")

    # 예외 있을 때 : try -> except -> finally
    # 예외 없을 때 : try -> else -> finally


def raise_exception():
    """
    예외의 위임
    """
    def beware_dog(animal): # animal == "dog" -> 강제 예외 발생 , 다른 동물이면 -> 컴온!
        if animal == "dog":  # 예외를 외부로 위임
            raise RuntimeError("강아지는 출입을 금한다!")
        else:
            print(animal, "Come On!")
    try:
        beware_dog("cat")
        beware_dog("cow")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))

    print("End of code")
if __name__ == "__main__":
    #hadling_exception()
    raise_exception()
