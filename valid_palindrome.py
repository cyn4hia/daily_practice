import string

def valid_palindrome(phrase):
    if phrase == " ":
        is_palindrome = False
        print(is_palindrome)
        return
    translator = str.maketrans('', '', string.punctuation + " ")
    cleaned = phrase.translate(translator)
    cleaned = cleaned.lower()
    half_length = int(len(cleaned) / 2)
    print(cleaned)
    is_palindrome = True
    for i in range(half_length):
        if cleaned[i] != cleaned[len(cleaned)-i-1]:
            is_palindrome = False
            break
    print(is_palindrome)


if __name__ == "__main__":
    phrase = "race a car"
    valid_palindrome(phrase)
    