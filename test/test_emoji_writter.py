from emoji_writer import (
    default_emoji_params,
    write_word,
    write_emoji_word,
    print_examples,
    list_emojis,
)


def test_write_word_defaults():
    default_params = default_emoji_params()
    emoji_word = write_word(
        "lgtm", default_params["foreground"], default_params["background"]
    )
    expected = """\
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜👍⬜⬜⬜⬜⬜⬜👍👍👍⬜⬜👍👍👍👍👍⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍👍⬜👍👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜👍👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜
⬜👍👍👍👍👍⬜⬜👍👍👍⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"""
    assert (
        emoji_word == expected
    ), f"write_emoji_word produced wrong result, expected: {expected}, got: {emoji_word}"


def test_write_word_defaults_with_boder():
    default_params = default_emoji_params()
    emoji_word = write_word(
        "lgtm",
        default_params["foreground"],
        default_params["background"],
        border_emoji="fire",
    )
    expected = """\
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
🔥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜⬜👍👍👍⬜⬜👍👍👍👍👍⬜👍⬜⬜⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍👍⬜👍👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜👍👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜🔥
🔥⬜👍👍👍👍👍⬜⬜👍👍👍⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜🔥
🔥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔥
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"""
    assert (
        emoji_word == expected
    ), f"write_emoji_word produced wrong result, expected: {expected}, got: {emoji_word}"


def test_write_word_with_spaces():
    default_params = default_emoji_params()
    emoji_word = write_word(
        "h o l a",
        "alien",
        "bright_button",
    )
    expected = """\
🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆🔆👽👽👽🔆🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆👽👽👽🔆🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽👽👽👽👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽👽👽👽👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆🔆👽👽👽🔆🔆🔆🔆🔆🔆👽👽👽👽👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆"""
    assert (
        emoji_word == expected
    ), f"write_emoji_word produced wrong result, expected: {expected}, got: {emoji_word}"


def test_multiline_same_length():
    emoji_word = write_emoji_word(
        word="asd\nfgh",
        foreground="thumbs_up",
        random_foreground=False,
        suggested_foreground=False,
        background="white_large_square",
        random_background=False,
        suggested_background=False,
        border=False,
        border_emoji="",
        border_size=1,
        random_border=False,
        emojize=True,
        emoji_source="uni_emoji",
    )
    expected = """\
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜👍👍👍⬜⬜⬜👍👍👍👍⬜👍👍👍👍⬜⬜
⬜👍⬜⬜⬜👍⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜👍⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜
⬜👍👍👍👍👍⬜⬜👍👍👍⬜⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜👍⬜⬜⬜⬜⬜👍⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜👍⬜⬜⬜⬜⬜👍⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜👍⬜👍👍👍👍⬜⬜👍👍👍👍⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜👍👍👍👍👍⬜⬜👍👍👍⬜⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜
⬜👍👍👍👍⬜⬜👍⬜⬜⬜⬜⬜👍👍👍👍👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜👍👍⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜⬜👍👍👍⬜⬜👍⬜⬜⬜👍⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"""

    assert (
        emoji_word == expected
    ), f"write_emoji_word produced wrong result, expected: {expected}, got: {emoji_word}"


def test_print_examples():
    """ test that it doesnt crash """
    print_examples()


def test_list_emojis():
    list_emojis("flags")


def test_list_emojis():
    list_emojis()
