def Quiz():
    # s = "Python Programming"  # 문자열 안 쪽에 몇 개의 알파벳이 사용되었는가?
    #chars = set(s.upper())
    #print(s, chars)

    s = "Life is too short You need Python"
    s.lower()\
        .replace(',', '').replace(" ", "").split()
    print(s, type(s))
    lst = list(s)
    print(s, type(s))
    chars = set(lst)
    print(chars, type(chars))
    lst.sort()
    print(chars, len(chars))

if __name__ == "__main__":
    Quiz()