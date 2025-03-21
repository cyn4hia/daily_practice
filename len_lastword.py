def len_lastword(s):
    s = s.split()
    last = s[len(s)-1]
    len_last = len(last)
    s[len(s)-1]
    print("the last word is " + last + " with a length of " + str(len_last))
    

if __name__ == "__main__":
    string = input("sentence: ")
    len_lastword(string)