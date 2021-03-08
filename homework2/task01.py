"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
from collections import defaultdict


def delete_first_and_last_symbol_if_they_are_not_characters(word: str) -> str:
    """Удаляет первый и послдений символы (кроме цифр) в переданной последовательности символов,
    если они не являются буквами"""
    word = list(word)
    if not word[0].isalpha() and not word[0].isdigit():
        del word[0]
    if not word[-1].isalpha() and not word[-1].isdigit():
        del word[-1]
    word = "".join(word)
    return word


def check_word_for_unique_symbols(word: str) -> bool:
    """Проверяет, состоит ли слово из уникальных символов"""
    set_of_characters_in_word = set()
    word = word.lower()
    word = delete_first_and_last_symbol_if_they_are_not_characters(word)
    if not word.isalpha():
        return False
    for character in word:
        if character in set_of_characters_in_word:
            return False
        else:
            set_of_characters_in_word.add(character)
    return True


def get_longest_diverse_words(file_path: str) -> List[str]:
    list_of_words_with_unique_symbols = []
    with open(file_path) as fi:
        for line in fi:
            print(line)
            list_of_words = line.split()
            print(list_of_words)
            for word in list_of_words:
                if check_word_for_unique_symbols(word):
                    list_of_words_with_unique_symbols.append(
                        delete_first_and_last_symbol_if_they_are_not_characters(word)
                    )
    list_of_words_with_unique_symbols.sort(key=len, reverse=True)
    list_of_longest_words_with_unique_symbols = list_of_words_with_unique_symbols[:10]
    return list_of_longest_words_with_unique_symbols


def get_rarest_char(file_path: str) -> str:
    dict_of_symbols = defaultdict(int)
    with open(file_path) as fi:
        for line in fi:
            for symbol in line:
                dict_of_symbols[symbol] += 1
    rarest_char = min(
        dict_of_symbols, key=dict_of_symbols.get
    )  # ищем ключ с минимальным значением
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    set_of_punctuation_chars = set(",.[]:`-–…!?();'")
    count_of_punctuation_chars = 0
    with open(file_path) as fi:
        for line in fi:
            for symbol in line:
                if symbol in set_of_punctuation_chars:
                    count_of_punctuation_chars += 1
    return count_of_punctuation_chars


def count_non_ascii_chars(file_path: str) -> int:
    count_of_non_ascii_chars = 0
    with open(file_path) as fi:
        for line in fi:
            for symbol in line:
                if ord(symbol) >= 128:
                    count_of_non_ascii_chars += 1
    return count_of_non_ascii_chars


def get_most_common_non_ascii_char(file_path: str) -> str:
    dict_of_symbols = defaultdict(int)
    with open(file_path) as fi:
        for line in fi:
            for symbol in line:
                if ord(symbol) >= 128:
                    dict_of_symbols[symbol] += 1
    common_char = max(
        dict_of_symbols, key=dict_of_symbols.values
    )  # ищем ключ с максимальным значением
    return common_char


start_dict={
  ('DD2', 'DD3'): 4, ('DD2', 'VD3'): 1, ('DD2', 'VD7'): 0,
  ('DD2', 'VD8'): 0, ('DD2', 'VD6'): 0, ('DD2', 'DD1'): 5,
  ('DD2', 'VD2'): 1, ('DD2', 'R1'): 1, ('DD2', 'VD4'): 1,
  ('DD2', 'VD5'): 0, ('DD2', 'R3'): 1, ('DD2', 'R4'): 0,
  ('DD2', 'VD1'): 1, ('DD2', 'R2'): 1
}
print(start_dict.get)