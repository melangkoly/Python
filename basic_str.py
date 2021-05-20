def define_str():
    # 한 줄 문자열의 정의
    s1 = "Helo Python"
    s2 = str("Hello Python")
    s3 = str(3.14159)

    print(s1, s2, s3)
    print(type(s1), type(s2), type(s3))

    print("s1 은 str의 객체 ", isinstance((s1, str)))

    #   여러 줄 문자열의 정의
    #   쌍다옴표 세 개 ("""), 홑따옴표 세 개(''')
    s4 = """Life is too short, you need python
    크크루삥뽕"""

    print(s4)

def String_oper():
    str1 = "Python"
    str2 = "Second String"

    # 길이
    print("str1 len", len(str1))

    # 변경 불가 자료형
    #str1[0] = 'f' -> error

    #인덱싱 : 배열과 비슷하게 인덱스로 접근 가능
    #인덱스의 범위 : 0 ~ len -1
    #print("정인덱싱 : ", str1[0], str1[1], str1[2], str[3], str1[4], str1[5])
    #print("역인뎅싱 : ", str1[-6], str[-5], str1[-4], str1[-3], str1[-2], str1[-1])


    print(str1[2 : 4])
    print(str1[-4 : -2])
    print(str1[0 : 3])
    print(str1[:3])
    print(str1[3 : len(str1)])
    print(str1[3 :])
    print(str1[:]) # 처음부터 끝까지
    # 슬라이싱  [시작경계 : 끝경계 : 간격]
    print(str1[::2])
    print(str1[::-2])

    #   연결(+) -> 산출 연산이 아님
    print(str1 + " Programming")
    #   반복(*)
    print((str1 * 3))

    print("P" in str1)
    print("P" not in str1)

def transform_ex():
    s = "I Like Python"
    print("원본", s)

    print("UPPER", s.upper())
    print("LOWER", s.lower())
    print("SWAPCASE", s.swapcase()) # 대문자 <> 소문자
    print("CAPITALIZE", s.capitalize()) # 문장의 첫 글자를 대문자로
    print("Title", s.title()) # 기사 제목 형태로 : 각 단어릐 첫 글자를 대문자로

    print("원본", s) #str 객체 immutable -> 원본이 변경되지는 않음

def search_methods():
    """
    문자열 검색 관련 메서드 연습
    """
    s = "I Like Python, I Like Java Too"
    print(s)
    print(s.count("Like")) # Like의 갯수
    print(s.find("Like")) # 문자열 내의 Like의 인덱스
    print(s.find("Like", 6)) # 6번 인덱스 이후의 Like의 인덱스
    print(s.find("Like", 20)) # 조건에 맞는 값이 없으면 -1

    print(s.index("Like"))
    print(s.index("Like", 6))
    #print(s.index("Like", 21)) # 검색 결과가 없으면 Error
    if "Like" in s[21:]: print(s.index("Like"), 21)

    #역방향 검색 : 찾는게 없으면 에러를 발생시킨다
    print(s)
    print(s.rfind("Like"))
    print(s.rfind("Like"), 0, 17) #0 ~ 17 경계 사이에서 Like를 검색

    #특정 문자열로 끝나는가?
    url = "http://www.naver.com"
    surl = "https://www.naver.com"
    ftp = "ftp://ftp.naver.com"

    print("url이 http로 시작하는가? ", url.startswith("http://"))
    print("surl이 https로 시작하는가? ", surl.startswith("https://"))

    # 검색시 시작 문자열을 여러개중 한개로 비교할때
    print("ftp가 http or https 로 시작하는가? ",
          ftp.startswith(("http://", "https://")))
    print("url이 http or https 로 시작하는가? ",
          url.startswith(("http://", "https://")))
    print("url이 naver.com으로 끝나는가?", url.endswith("naver.com"))
    # 검색 범위를 제한할 수도 있다
    print(ftp.startswith("ftp", 6, 20)) # 6 ~ 20 경계 영역이 ftp로 시작?

def modify_replace_mothods():
    """
    문자열 수정, 치환 관련 메소드들
    """
    s = "              Alice and the Heart Queen          "
    print("STRIP:[", s.strip(), "]", sep = "") #앞 뒤의 공백 문자 제거
    print("LStrip : [", s.lstrip(), "]", sep = "") # 왼쪽 (앞)의 공백문자 제거
    print("RStrip : [", s.rstrip(), "]", sep = "") #    오른쪽 제거

    s = "I Love Java"
    print(s)
    print(s.replace("Java", "Python")) # 원본은 변경되지 않음

def split_join_methods():
    """
    분할과 합치기 메소드
    """
    s = "Ham and Cheese and Breads and Ketchup"

    print(s)
    print("Split", s.split()) # 기본적으로 공백으로 분리
    items = s.split(" and ")
    print("Split", items)

    items = s.split(" and ", 2) # and 구분자를 기준으로 앞으로부터 2개만 추출
    print(items)
    items = s.rsplit(" and ", 2) # 뒤로부터 2개만 추출
    print(items)
    lines = """
    Java Programming
    Python Programming
    Oracle Programming
    """

    print(lines.split()) #공백문자 (스페이스, 탭, 개행)
    print(lines.splitlines()) # 기본적으로는 개행문자를 유지 안함
    print(lines.splitlines(True)) # 개행문자 삭제하지 않음

def check_method(): #판별 관련 -> is 계열 메소드 -> bool
    print("1234567890".isdigit()) # 문자열이 숫자만 사용하는가
    print("abcdefg".isalpha()) # 문자열이 알파벳만 사용하는가
    print("Python3".isalnum()) # 문자열이 알파벳 + 숫자만 포함?
    print("Python 3".isalnum()) #  공백 포함 -> alnum이 아님
    print(" r\n\t".isspace()) #공백문자만 포함?
    print(" ".isspace())
    print("python".islower())
    print("PYTHON".isupper())
    print("Python Programming".istitle())

def align_methods():
    """
    문자열 정렬 메소드
    """
    s = "Alice and the Heart Queen"

    print(s.center(60), sep = "") # 60자리 확보 정렬
    print(s.center(60, "*"), sep = "") # 빈자리를 * 로 채우기
    print(s.ljust(60, "*"), sep = "") # 왼쪽 정렬
    print(s.rjust(60, "*"), sep = "") # 오른쪽 정렬

    print("1234".zfill(5)) # 5자리 확보, 내용을 채운 후 빈자리는 0으로 채운다
    print("1234567890".zfill(5)) # 확보한 자리는 최소 공간, 자리수 넘쳐도 잘리지 않음


if __name__ == "__main__":
    #define_str()
    #String_oper()
    #transform_ex()
    #search_methods()
    #modify_replace_mothods()
    #split_join_methods()
    #check_method()
    align_methods()