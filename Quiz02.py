def q1():
    score1 = int(input("점수 :"))
    score2 = int(input("점수 :"))

    average = (score1 + score2) / 2

    if score1 >= 50 and \
        score2 >= 50 and \
        average >= 60:
        m = "합격"
    else:
        m = "불합격"

    print(m)

def gugudan():
    for i in range(2, 10):
        print(i)
        for n in range(1, 10):
            print("{} x {} : {}".format(i, n, i * n))


def mugen():
    balance = 1000
    while True:  # 무한 루프
        method = input("method : ")
        if method == 'q':
            break # 루프 종료
        if method != 'd' and method != 'w':
            print("?")
            continue
        # d, w 만 남음
        # 금액 입력
        amount = int(input("Amount :"))

        balance += amount if method == "d" else -amount

        print("Balance :", balance)

    print("프로그램 종료")



if __name__ == "__main__":
    #q1()
    #gugudan()
    mugen()