"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import defaultdict
from typing import List


def get_clear_word(word: str) -> str:
    """Takes a string, if there are symbols before or after this string, deletes them,
    if they are not characters or digits, and returns clear word, also if string consists only from non
    chars or digits, it will return empty string"""
    word = list(word)
    while not word[0].isalpha() and not word[0].isdigit():
        del word[0]
        if len(word) == 0:
            word = "".join(word)
            return word
    while not word[-1].isalpha() and not word[-1].isdigit():
        del word[-1]
    word = "".join(word)
    return word


def check_word_for_unique_symbols(word: str) -> bool:
    """Takes a string, checks, if the string consists only form unique symbols, using set of its
    characters, and returns bool"""
    set_of_characters_in_word = set()
    word = word.lower()
    word = get_clear_word(word)
    if not word.isalpha():
        return False
    for character in word:
        if character in set_of_characters_in_word:
            return False
        else:
            set_of_characters_in_word.add(character)
    return True


def get_longest_diverse_words_from_file(file_path: str) -> List[str]:
    """Takes a file path, finds in the file all the words, consisting
    from the unique chars (using 'check_word_for_unique_symbols' function), puts these words in a list,
    sorts this list in descending order by length of the words and returns slice of first ten words of the list"""
    list_of_words_with_unique_symbols = []
    with open(file_path, "rb") as fi:
        for line in fi:
            list_of_words = line.decode("unicode-escape").split()
            for word in list_of_words:
                if check_word_for_unique_symbols(word):
                    list_of_words_with_unique_symbols.append(get_clear_word(word))
    list_of_words_with_unique_symbols.sort(key=len, reverse=True)
    list_of_longest_words_with_unique_symbols = list_of_words_with_unique_symbols[:10]
    return list_of_longest_words_with_unique_symbols


def get_rarest_char_from_file(file_path: str) -> str:
    """Takes a file path, creates dict of symbols with key = 'symbol' and
    value = 'count of the appearance of this symbol', finds the rarest symbol
    from the dict by the value and returns the rarest symbol"""
    dict_of_symbols = defaultdict(int)
    with open(file_path, "rb") as fi:
        for line in fi:
            for symbol in line.decode("unicode-escape"):
                dict_of_symbols[symbol] += 1
    if not bool(dict_of_symbols):
        return ""
    rarest_char = min(
        dict_of_symbols, key=dict_of_symbols.get
    )  # ищем ключ с минимальным значением
    return rarest_char


def count_punctuation_chars_from_file(file_path: str) -> int:
    """Takes a file path, counts how many punctuation chars are in the file, using set of punctuation chars,
    and returns the count"""
    set_of_punctuation_chars = set(",.[]:`-–…!?();'")
    count_of_punctuation_chars = 0
    with open(file_path, "rb") as fi:
        for line in fi:
            for symbol in line.decode("unicode-escape"):
                if symbol in set_of_punctuation_chars:
                    count_of_punctuation_chars += 1
    return count_of_punctuation_chars


def count_non_ascii_chars_from_file(file_path: str) -> int:
    """Takes a file path, counts how many non ascii chars are in the file, using method 'ord', and returns the count"""
    count_of_non_ascii_chars = 0
    with open(file_path, "rb") as fi:
        for line in fi:
            for symbol in line.decode("unicode-escape"):
                if ord(symbol) >= 128:
                    count_of_non_ascii_chars += 1
    return count_of_non_ascii_chars


def get_most_common_non_ascii_char_from_file(file_path: str) -> str:
    """Takes a file path, creates dict of symbols with key = 'symbol' and
    value = 'count of the appearance of this symbol', finds the most common non
    ascii char (using method 'ord') from the dict by the value, and returns this symbol"""
    dict_of_symbols = defaultdict(int)
    with open(file_path, "rb") as fi:
        for line in fi:
            for symbol in line.decode("unicode-escape"):
                if ord(symbol) >= 128:
                    dict_of_symbols[symbol] += 1
    if not bool(dict_of_symbols):
        return ""
    common_char = max(
        dict_of_symbols, key=dict_of_symbols.get
    )  # ищем ключ с максимальным значением
    return common_char
