def Quiz():
   # s = "Python Programming"  # 문자열 안 쪽에 몇 개의 알파벳이 사용되었는가?
    #chars = set(s.upper())
    #print(s, chars)

    str = "Life is too short You need Python"
    chars = set(str.lower())
    print(str, chars)
    print(len(chars))
   
if __name__ == "__main__":
    Quiz()