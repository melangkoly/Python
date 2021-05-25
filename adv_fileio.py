# 파일 모드
# action : r(읽기 : 디폴트 값), w(쓰기), a(추가)
# type : t(텍스트 : 디폴트), b(바이너리)

def write01():
    f = open("./sample/test.txt", "w", encoding="UTF-8") # write txt
    write_size = f.write("Life is too short, You need Python")
    print(write_size)
    f.close()

def write02():
    f = open("./sample/multilines.txt", "w", encoding="UTF-8")
    for i in range(10):
        f.write("Line %d\n" % i)
    f.close()

def read01():
    f = open("./sample/multilines.txt", "r", encoding="UTF-8")
    text = f.read()
    print(text)
    f.close()

def read02():
    # 읽고자 하는 파일이 대용량일 경우
    # readline 메소드를 이용하면 한 줄 단위로 읽을 수 있다. 'ㅅ';
    f = open("./sample/multilines.txt", 'r', encoding="UTF-8")
    while True:
        line = f.readline() # 한 줄 단위 읽기
        if not line: # 읽을 내용이 없으면
            break
        print(line)
    f.close()

def read03():
    # readlines 메소드 -> 전체 리스트를 불러와서 리스트로 변환 제공
    f = open("./sample/multilines.txt", 'r', encoding="UTF-8")
    lines = f.readlines()

    for line in lines:
        print(line)
    f.close()

def copy_binary():
    # Binary 파일을 다루려면 모드를 b로 생성
    # rose-flower.jpeg -> rose-flower-copy.jpeg로 복사
    f_src = open("./sample/rose-flower.jpeg", 'rb') # read binary 모드로 설정
    data = f_src.read()
    print(type(data))
    f_src.close()

    f_dest = open("./sample/rose-flower-copy.jpeg", "wb")
    f_dest.write(data)
    f_dest.close()

if __name__ == "__main__":
    #write01()
    #write02()
    #read01()
    #read02()
    #read03()
    copy_binary()