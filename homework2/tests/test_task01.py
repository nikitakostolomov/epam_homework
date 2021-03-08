import pytest
import task01


@pytest.mark.parametrize(
    ["word", "expected_result"],
    [
        ("privet", "privet"),
        ("kek)", "kek"),
        (",Lol", "Lol"),
        (")privet)", "privet"),
        ("privet)))", "privet))"),
        ("1kak", "1kak"),
    ],
)
def test_delete_first_and_last_symbol_if_they_are_not_characters(
        word: str, expected_result: str
):
    actual_result = task01.delete_first_and_last_symbol_if_they_are_not_characters(word)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["word", "expected_result"],
    [
        ("privet", True),
        ("kek", False),
        ("Lol", False),
        ("privet)", True),
        ("privet)))", False),
    ],
)
def test_check_word_for_unique_symbols(word: str, expected_result: bool):
    actual_result = task01.check_word_for_unique_symbols(word)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("data_for_task01/data01", ["noviy", "dela", "dela", "eto"]),
        (
                "data_for_task01/data02",
                ["Gnealz", "right", "beat", "Yuh", "Yuh", "yuh", "the", "Yuh", "it", "on"],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: list):
    actual_result = task01.get_longest_diverse_words(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("data_for_task01/data03", "\n"),
        ("data_for_task01/data01", ","),
    ],  # перенос строки считается символом?)
)
def test_get_rarest_char(file_path: str, expected_result: str):
    actual_result = task01.get_rarest_char(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_for_task01/data01", 1), ("data_for_task01/data02", 16), ("data_for_task01/data03", 2)]
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    actual_result = task01.count_punctuation_chars(file_path)
    assert actual_result == expected_result
