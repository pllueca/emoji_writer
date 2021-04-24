from emoji_writer import default_emoji_params, write_word


def test_write_word_defaults():
    default_params = default_emoji_params()
    emoji_word = write_word(
        "lgtm", default_params["foreground"], default_params["background"]
    )
    expected = """⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜👍⬜⬜⬜⬜⬜⬜👍👍👍⬜⬜👍👍👍👍👍⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍👍⬜👍👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜👍👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜
⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜
⬜👍👍👍👍👍⬜⬜👍👍👍⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
"""
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
    expected = """🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
🔥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜⬜👍👍👍⬜⬜👍👍👍👍👍⬜👍⬜⬜⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍👍⬜👍👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜👍⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜👍👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜🔥
🔥⬜👍⬜⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜🔥
🔥⬜👍👍👍👍👍⬜⬜👍👍👍⬜⬜⬜⬜👍⬜⬜⬜👍⬜⬜⬜👍⬜🔥
🔥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🔥
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
"""
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
    expected = """🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆🔆👽👽👽🔆🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆👽👽👽🔆🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽👽👽👽👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽👽👽👽👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆🔆🔆🔆🔆🔆👽👽👽🔆🔆🔆🔆🔆🔆👽👽👽👽👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆
"""
    assert (
        emoji_word == expected
    ), f"write_emoji_word produced wrong result, expected: {expected}, got: {emoji_word}"

def test_multiline_same_length():
    default_params = default_emoji_params()
    emoji_word = write_word(
        "asd\nfgh",
        default_params["foreground"],
        default_params["background"],
    )
    expected = """⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
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
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
"""

    assert (
        emoji_word == expected
    ), f"write_emoji_word produced wrong result, expected: {expected}, got: {emoji_word}"
