def subtract_product_and_sum(num):
    product = 1
    sum = 0
    string_num = str(num)
    
    for i in range(len(string_num)):
        sum += int(string_num[i])
        product *= int(string_num[i])
    
    print(product - sum)
   

if __name__ == "__main__":
    num = 4421
    subtract_product_and_sum(num)