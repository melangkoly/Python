def Quiz2():

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("ORI : ", lst)
    slice = lst[3 : 7]
    slice.reverse()
    lst[3 : 7] = slice
    print(lst)


if __name__ == "__main__":
    Quiz2()
