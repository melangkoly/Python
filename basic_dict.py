def define_dict():
    """
    사전 생성 연습
    """
    # 빈 사전
    dct = dict()
    print(dct, type(dct))
    # Literal 이용 : {}
    dct = {"basketball" : 5, "baseball": 9}

    # 순서가 없고 인덱스가 아닐 키를 이용해서 내용에 접근
    dct['volleyball'] = 6
    print(dct)
    # 길이 확인 가능
    # 연결 및 반복은 불가능
    print("LENGTH : ", len(dct))
    print("soccer 키가 있는가?", "soccer" in dct)
    print("baseball 키가 있는가?", "baseball" in dct)

    # 키의 목록, 값의 목록
    print("키의 목록 : ", dct.keys(), type(dct.keys()))
    print("값의 목록 : ", dct.values(), type(dct.values()))
    print("(키, 값) 쌍튜플의 목록 :", dct.items(), type(dct.items()))

    # 응용
    # 포함 여부는 key
    # 사전의 값의 포함 여부를 확인하려면?
    # dct 의 값 중에서 9 값이 포함되어 있는지 확인하려면?
    print("9 in 값 목록 :", 9 in dct.values())

    # 키워드 인자를 이용한 사전의 생성
    d1 = dict(key1 = "value1", key2 = "value2")
    print(d1, type(d1))

    # 튜플의 리스트를 이용한 사전의 생성
    d2 = dict([('key1', 'value1'), ('key2', 'value2')])
    print(d2, type(d2))

    # 키 목록 , 값 목록 있을 때 -> zip 객체 이용
    keys = ('one', 'two', 'three')
    values = (1, 2, 3, 4)
    d3 = dict(zip(keys, values))
    print(d3, type(d3))

    # 사전의 키 : 변경 불가 객체만 사용 가눙
    d4 = {}
    d4[True] = "true"
    d4[10] = 10
    d4['eleven'] = 11
    d4[(10, '홍길동')] = 100

    # list 등 가변 객체는 사용 불가
    #d4([1, 2, 3]) = 100 -> 에러

def dict_methods():
    """
    사전의 메소드
    """
    dct = {'soccer' : 5, 'baseball': 9, 'volleyball' : 6}
    print(dct)
    # 사전의 키 목록 : keys()
    keys = dct.keys()
    print("키 목록 : ", keys, type(keys))
    # dict_keys   역시 순차형 -> 다른 순차형으로 변환 가능
    lst_keys = list(keys) # dict_keys 타입을 list로 변환
    print(lst_keys, type(lst_keys))

    # 사전의 값 목록 : values()
    values = dct.values()
    print("값의 목록 : ", values, type(values))

    # (키, 값) 쌍 튜플의 목록 : items()
    items = dct.items()
    print("(키, 값) 의 목록 : ", items, type(items))
    lst_items = list(items)
    print(lst_items, type(lst_items))
    #튜플의 리스트 -> 인덱스 접근 가능
    print("Key : ", lst_items[0][0], "Value :", lst_items[0][1])
    # 사전 비우기
    dct.clear()
    print(dct)

def using_dict():
    phones = {
        "둘리" : "010-1234-5678",
        "도우너" : "010-9876-543",
        "또치" : "010-2222-3333"
    }
    print(phones)

    #새로운 항목 추가
    phones['고길동']  = "032-1234-5677"
    print(phones)

    # 키에 접근 vs get() 메소드
    print("둘리", phones["둘리"])
    #print("홍길동", phones['홍길동']) # 없는 키에 접근 - > 에러
    print("홍길동", phones.get('홍길동')) # 없는 키지만 None을 반환
    # get 메소드를 사용하는 이유
    # 1. key가 없어도 에러가 뜨지 않음
    # 2. 기본 값 기능이 있어서 None 값을 받고 싶지 않을 때
    print("홍길동", phones.get("홍길동", '전화 없음')) # Key가 없으면 기본 값을 반환

    # 삭제
    del phones['도우너'] # 도우너 키 삭제
    print(phones)

    # 값을 가져오며 삭제 : POP
    print(phones.pop('둘리')) # 둘리 키의 값을 빼내고 키 삭제
    print(phones)

def loop():
    """
    사전의 순회
    """
    phones = {
        "둘리": "010-1234-5678",
        "도우너": "010-9876-543",
        "또치": "010-2222-3333"
    }
    print("원본 : ", phones)

    # 기본적인 루프 생성 - > 기본은 key
    for key in phones:
        print(key + " : " + phones.get(key))
    else:
        print()

    # 사전으로부터 키의 목록을 리스트로 받아온 후 출력
    for key in phones.keys():
        print(key + " : " + phones.get(key))
    else:
        print()

    # 키와 값 쌍 튜플을 받아와서 출력
    for(key, value) in phones.items(): # Unpacking
        print(key + " : " + value)

if __name__ == "__main__":
    #define_dict()
    #dict_methods()
    #using_dict()
    loop()