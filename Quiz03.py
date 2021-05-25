def q1():
    while True:
        i = int(input("정수 :"))
        try:
            int(i)  # 캐스팅
        except ValueError as e:
            print("정수가 아닙니다. 재입력하세요")
        else:  # try 블록에 예외가 없을 시
            break
    total = 0
    to = int(i)

    #for n in range(1, to + 1):  # 1 ~ to
       # if n % 3 == 0:
            #total += n
    lst = [ i for i in range(1, to + 1) if i % 3 == 0] # 3의 배수 list
    total = sum(lst)

    print("1부터 {}까지의 3의 배수 합 :  {}".format(to, total))

def q2():
    lst = [1, 3.14, 'python', 7, 89.1, 3]
    lst_cleaned = []
    #for item in lst:
        #if isinstance(item, (int, float))
            #lst_cleaned.append(item)
    lst_cleaned = [ item for item in lst if isinstance(item, (int, float))]
    print("cleaned : ", lst_cleaned)

def summary(*args):
    total = sum(args)
    return total, max(args), min(args), total / len(args)

def q3():
    total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
    print(total, maxval, minval, avg)

def q4():
    s = """We encourage everyone to contribute to Python. 
    If you still have questions after reviewing the material
    in this guide, then the Python Mentors 
    group is available to help guide new contributors through the process."""

    # 정제
    s = s.replace(",", "").replace(".", "").replace("\n", "").upper()
    splits = s.split()
    print("splits: ", splits)
    summary = {} # 결과 사전
    for word in splits:
        if word in summary.keys(): # 이미 키에 있으면
            summary[word] += 1
        else:
            summary[word] = 1

    for key, value in summary.items(): #(key, value) 튜플
        print("{} : {}".format(key, value))


if __name__ == "__main__":
    #q1()
    #q2()
    #q3()
    q4()
