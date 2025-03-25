def find_fizzbuzz(n):
    fizzbuzz = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                fizzbuzz.append("Fizzbuzz")
            else:
                fizzbuzz.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz.append("Buzz")
        else:
            fizzbuzz.append(i)
    print(fizzbuzz)

if __name__ == "__main__":
    integer = int(input("input number: "))
    find_fizzbuzz(integer)