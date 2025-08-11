def check_prefix(sentence, prefix):
    words = 1
    word_found = False
    for i in range(len(sentence)):
        if sentence[i] == " ":
            words += 1
        if prefix == sentence[i:i+(len(prefix))]:
            print(words)
            word_found = True
            break
    if word_found == False:
        print(-1)

if __name__ == "__main__":
    message = "i am tired"
    search_word = "you"
    check_prefix(message, search_word)