import array
import numpy as np


def find_median():
    array_one = [3, 15, 7, 10, 2, 9]
    array_two = [1, 2, 3, 4, 5, 6, 10]   
    merged_array = []
    
    for i in range(len(array_one)):
        merged_array.append(array_one[i])

    for j in range(len(array_two)):
        merged_array.append(array_two[j])

    merged_array.sort()
    print(merged_array)
    # max = 0
    
    # for i in range(len(merged_array)):
    #     for j in range(len(merged_array)):
    #         if merged_array[max] > merged_array[j]:
    #             temp = merged_array[max]
    #             merged_array[max] = merged_array[j]
    #             merged_array[j] = temp
    #             #max = j
    #         elif merged_array[max] < merged_array[j]:
    #             temp = merged_array[max]
    #             merged_array[max] = merged_array[j]
    #             merged_array[j] = temp
    #             max = j


                
            # elif merged_array[max] > merged_array[j]:
            #     temp = merged_array[max]
            #     merged_array[max] = merged_array[j]
            #     merged_array[j] = temp
        # print(merged_array[max])
        # print(merged_array)
    if len(merged_array) % 2 == 1:
        median = (merged_array[int(len(merged_array)/2)])
        print(median)
    else:
        median = (merged_array[int(len(merged_array)/2)] + merged_array[int(len(merged_array)/2 - 1)]) / 2 
        print(median)


    # image = [[1, 2, 3], [4,5,6], [7,8,9]]
    
    # print(merged_array)
            


if __name__ == "__main__":
    find_median()

