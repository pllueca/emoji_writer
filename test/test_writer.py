from emoji_writer import Writer


def test_default():
    background = "⬜"
    foreground = "👍"

    w = Writer(foreground, background)
    emoji_word = w.write_line("LGTM")

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


def test_default_with_border():
    background = "⬜"
    foreground = "👍"
    border = "🔥"

    w = Writer(foreground, background, border_emoji=border, border_size=1)
    emoji_word = w.write_line("LGTM")

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


def test_thick_border():

    background = "👍"
    foreground = "⬜"
    border = "👽"

    w = Writer(foreground, background, border, 3)
    emoji_word = w.write_line("LGTM")
    expected = """\
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽
👽👽👽👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👽👽👽
👽👽👽👍⬜👍👍👍👍👍👍⬜⬜⬜👍👍⬜⬜⬜⬜⬜👍⬜👍👍👍⬜👍👽👽👽
👽👽👽👍⬜👍👍👍👍👍⬜👍👍👍⬜👍👍👍⬜👍👍👍⬜⬜👍⬜⬜👍👽👽👽
👽👽👽👍⬜👍👍👍👍👍⬜👍👍👍👍👍👍👍⬜👍👍👍⬜👍⬜👍⬜👍👽👽👽
👽👽👽👍⬜👍👍👍👍👍⬜👍👍👍👍👍👍👍⬜👍👍👍⬜👍⬜👍⬜👍👽👽👽
👽👽👽👍⬜👍👍👍👍👍⬜👍👍⬜⬜👍👍👍⬜👍👍👍⬜👍👍👍⬜👍👽👽👽
👽👽👽👍⬜👍👍👍👍👍⬜👍👍👍⬜👍👍👍⬜👍👍👍⬜👍👍👍⬜👍👽👽👽
👽👽👽👍⬜⬜⬜⬜⬜👍👍⬜⬜⬜👍👍👍👍⬜👍👍👍⬜👍👍👍⬜👍👽👽👽
👽👽👽👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👽👽👽
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽"""
    assert (
        emoji_word == expected
    ), f"write_emoji_word produced wrong result, expected: {expected}, got: {emoji_word}"


def test_with_spaces():
    background = "🔆"
    foreground = "👽"

    w = Writer(foreground, background)
    emoji_word = w.write_line("H O L A")

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
