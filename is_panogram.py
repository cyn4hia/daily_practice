def is_panogram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict = {}
    for i in alphabet:
        dict[i] = False

    print(dict)
    for j in sentence:
        if dict[j] == False:
            dict[j] = True
    
    for k in alphabet:
        if dict[k] == False:
            return False

    return True

if __name__ == "__main__":
    sentence = "leetcode"
    print(is_panogram(sentence))
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(is_panogram(sentence))
