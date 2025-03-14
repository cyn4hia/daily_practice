def find_three_sum(values):

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            for k in range(j+1, len(values)):
                if values[i]+values[j]+values[k] == 10:
                    print("the indexes are " + str(i) + " and " + str(j) + " and " + str(k))



if __name__ == "__main__":
    values = [1,2,3,4,6,7]
    find_three_sum(values)