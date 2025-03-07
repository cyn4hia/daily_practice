def rotate():
    list_store = []
    # for i in range(len(list)):
    #     list_store.append(list[i])
    
    # col1 = []
    # col2 = []
    # col3 = []

    # for i in range(3):
    #     col1.append(list[2-i][0])
    #     col2.append(list[2-i][1])
    #     col3.append(list[2-i][2])

    # list2 = []
    # list2.append(col1)
    # list2.append(col2)
    # list2.append(col3)
    # print(list2)
    m = len(list)
    
    # print(m)
    for i in range(m):
        col = []
        for j in range(m):
            col.append(list[m-j-1][i])
        list_store.append(col)
    print(list_store)




if __name__ == "__main__":
    list = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    rotate(list)
