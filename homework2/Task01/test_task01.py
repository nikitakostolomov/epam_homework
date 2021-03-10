import pytest
import Task01.task01 as task01


@pytest.mark.parametrize(
    ["word", "expected_result"],
    [
        ("privet", "privet"),
        ("kek)", "kek"),
        (",Lol", "Lol"),
        (")privet)", "privet"),
        ("...privet)))", "privet"),
        ("1kak", "1kak"),
        ("mu\u00df", "mu\u00df"),
        ("mu\u00df!", "mu\u00df"),
        (",,!,", ""),
    ],
)
def test_get_clear_word(word: str, expected_result: str):
    """Checks, if from the given word, function will delete symbols in the beginning and in the end,
    but only if they are not letters or digits, and return empty word, if it`s consisting only from
    non digits or chars"""
    actual_result = task01.get_clear_word(word)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["word", "expected_result"],
    [
        ("privet", True),
        ("kek", False),
        ("Lol", False),
        ("privet)", True),
        ("privet)))", True),
        ("mu\u00df", True),
    ],
)
def test_check_word_for_unique_symbols(word: str, expected_result: bool):
    """Checks if the word consists only from unique symbols"""
    actual_result = task01.check_word_for_unique_symbols(word)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("Task01/Data_for_task01/data01", ["abcde", "abcd", "abc", "m\u00df"]),
        (
            "Task01/Data_for_task01/data02",
            [],
        ),
        (
            "Task01/Data_for_task01/data",
            [
                "verständlich",
                "kalyptischen",
                "Zwickmühlen",
                "Verdichtung",
                "unsichtbare",
                "anschuldigt",
                "übermächtig",
                "aufschließt",
                "Schilderung",
                "Schilderung",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: list):
    """Checks if from the given file function will find there up to 10 longest words,
    consisting from the unique symbols"""
    actual_result = task01.get_longest_diverse_words_from_file(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("Task01/Data_for_task01/data02", ""),
        ("Task01/Data_for_task01/data03", "\r"),
        ("Task01/Data_for_task01/data04", "\u00fc"),
        ("Task01/Data_for_task01/data", "›"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    """Checks if from the given file function will return the rarest symbol"""
    actual_result = task01.get_rarest_char_from_file(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("Task01/Data_for_task01/data01", 3),
        ("Task01/Data_for_task01/data02", 0),
        ("Task01/Data_for_task01/data03", 2),
        ("Task01/Data_for_task01/data", 5306),
    ],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    """Checks if from the given file function will count all punctuation chars and return this count"""
    actual_result = task01.count_punctuation_chars_from_file(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("Task01/Data_for_task01/data01", 1),
        ("Task01/Data_for_task01/data02", 0),
        ("Task01/Data_for_task01/data03", 0),
        ("Task01/Data_for_task01/data", 2972),
    ],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    """Checks if from the given file function will count all non ascii chars and return this count"""
    actual_result = task01.count_non_ascii_chars_from_file(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("Task01/Data_for_task01/data01", "\u00df"),
        ("Task01/Data_for_task01/data02", ""),
        ("Task01/Data_for_task01/data04", "\u00ab"),
        ("Task01/Data_for_task01/data", "ä"),
    ],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    """Checks if from the given file function will fine most common non ascii symbol and return this symbol"""
    actual_result = task01.get_most_common_non_ascii_char_from_file(file_path)
    assert actual_result == expected_result
