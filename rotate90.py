def rotate():
    list = [[1,2,3], [4,5,6], [7,8,9]]

    col1 = []
    col2 = []
    col3 = []
    
    for i in range(3):
        col1.append(list[2-i][0])
        col2.append(list[2-i][1])
        col3.append(list[2-i][2])

    list2 = []
    list2.append(col1)
    list2.append(col2)
    list2.append(col3)
    print(list2)
    


if __name__ == "__main__":
    rotate()