def richest_customer(accounts):
    temp = 0
    total_bal = []
    greatest = [0, 0]
    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            temp += accounts[i][j]
        
        if temp > int(greatest[1]):
            greatest[1:3] = [i, temp]
        total_bal.append(temp)
        print(str(i+1) + "st customer has wealth = " + str(total_bal[i]))
        temp = 0
    print("The " + str(i+1) + "nd richest customer with a weath of " + str(total_bal[i]))
    

if __name__ == "__main__":
    accounts = [[1,3], [2,5], [8,9]]
    richest_customer(accounts)
    