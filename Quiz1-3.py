def Quiz03():
    fruit = ["사과", "사과", "바나나", "바나나", "딸기", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

    d = {}

    for f in fruit:
        if f in d:  # "사과" 라는 key가 d 라는 딕셔너리에 있나?
            d[f] = d[f] + 1  # 그럼 "사과" 갯수를 하나 올려줘
        else:
            d[f] = 1  # 만약 "사과"라는 애가 없으면 그걸 딕셔너리에 넣고 밸류를 1로 만들어

    print(d)







if __name__ == "__main__":
    Quiz03()