def subtract_product_and_sum(num):
    # Given an integer number n, return the difference between the product of its digits and the sum of its digits.
    product = 1
    sum = 0
    string_num = str(num)
    
    for i in string_num:
        sum += int(i) 
        product *= int(i)
    
    return product - sum

if __name__ == "__main__":
    num = 4421
    print(subtract_product_and_sum(num))