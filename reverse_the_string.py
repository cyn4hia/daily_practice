def reverse_the_string(s):
    s_len = int(len(s)/2)
    for i in range(s_len):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    print(s)
if __name__ == "__main__":
    message = ["H","a","n","n","a","h"]
    reverse_the_string(message)