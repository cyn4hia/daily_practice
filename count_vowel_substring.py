from typing import Dict

def count_vowel_substring(word: str) -> int:
    """
    Count the distinct substrings containing only vowels in a string.

    Args:
        word (str): word that will be tested to find the number of distinct substrings

    Returns:
        int: num of distinct substrings

    """
    word_substrings = []

    for i in range(len(word)):
        temp: str = ""
        a_map: Dict = {"a": False, "e": False, "i": False, "o": False, "u": False}
        for j in range(i, len(word)):

            if a_map.get(word[j], None) is None:
                break

            a_map[word[j]] = True
            temp += word[j]

            if all(a_map.values()):
                if not temp in word_substrings:
                    word_substrings.append(temp)

    print(word_substrings)
    return len(word_substrings)

if __name__ == "__main__":
#    word = "cuaieuouac"
    _input : str = "aeiouaeiou"
    print(count_vowel_substring(_input))
