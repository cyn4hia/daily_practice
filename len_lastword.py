def len_lastword(s):
    s = s.split()
    last = s[len(s)-1]
    len_last = len(last)
    s[len(s)-1]
    print("the last word is " + last + " with a length of " + str(len_last))
    
def test_exception(val:int): 
    if val < 5:
        raise ValueError
    return val


if __name__ == "__main__":
    # string = input("sentence: ")
    # len_lastword(string)
    val : int = 4
    try:
        test_exception(val)
        print ("value %d is good", val)
    except ValueError:
        print ("value %d shall not less than 5", val)
    finally:
        print("end")