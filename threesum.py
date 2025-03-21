def find_three_sum(values, target):

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            for k in range(j+1, len(values)):
                if values[i]+values[j]+values[k] == target:
                    print("the indexes are " + str(i) + " and " + str(j) + " and " + str(k))



if __name__ == "__main__":
    values = [1,2,3,4,6,7]
    find_three_sum(values, 10)
