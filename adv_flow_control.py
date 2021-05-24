def if_statement():
    """
    if 문 연습
    """
    # 금액을 입력받고
    # 10000원 이상이면 by taxi
    # 1000원 이상이면 by bus
    # 그 미만이면 on foot을 출력
    money = int(input("너 얼마 있냐 ? "))

    message = " "
    if money > 10000:
        message = "by taxi"
    elif money > 1000:
        message = "by bus"
    else:
        message = "on foot"

    print(message)

def cond_expr(): # 조건 표현식
    # C, JAVA 의 3항 연산식과 비슷한 역할
    money = int(input("너 얼마 있냐 ? "))

    message = "by taxi" if money > 10000 else "by bus" if money >= 1000 else "on foot"
    print(message)

def for_ex():
    """
    for 반복문
    """
    # syntax : for 변수 in 순차형:
    a = ['cat', 'cow', "tiger"]
    for animal in a:
        print(animal, end=' ')
    else: #    반복문이 break 되지 않고 정상 종료시 마지막에 수행
        print()

    # 반복시 요소와 함께 인덱스도 함께 필요할 때 -> enumerate() -> (Index, parameter) 튜플
    for index, color in enumerate(['red', 'blue', 'green', 'black', 'white']):
        print(index, color)

    # range 객체 (범위 객체)
    # 1 ~ 10 까지 합 구하기
    total = 0
    for i in range(1, 11): # 1 ~ 10 까지 반복
        total += i

    print("total: ", total)

    # break : 남은 루프를 진행하지 않고 반복문 탈출!
    r1 = list(range(1, 12, 2)) + [12, 13, 15]
    print("r1 : ", r1)
    # 첫번 째 짝수를 출력
    for i in r1:
        if i % 2 == 0:
            print("첫 번째 짝수를 찾았다: ", i)
            break # 루프 탈출
    else:
        print("짝수는 없다") # 일단 루프를 탈출하면 실행되지 않음

    # continue : 남은 실행문은 실행하지 않고 다음번 루프 돌림
    # 0 ~ 10 범위 중에서 짝수는 제외하고 값 출력
    for i in range(11):
        if i % 2 == 0:
            continue
        print(i, end= ' ')
    else:
        print()


    #for i in range(10):

def while_ex():
    """
    while 문 연습
    """
    # 연습문제 1. 2 ~ 9 단 구구단표 출력
    # 연습문제 2. 삼각형 출력


if __name__ == "__main__":
    #if_statement()
    #cond_expr()
    #for_ex()
    while_ex()