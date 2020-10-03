""" Python emoji writter.
write works in 7x5 grids, with emojis
"""
from typing import Dict, List, Tuple
import sys
import random

import emoji

from .letters import letters_to_matrix, EMPTY_LETTER


def get_emoji_list(emoji_source: str) -> list:
    """ get list of emoji name based on specified type """
    if emoji_source == "uni_emoji":
        return list(emoji.unicode_codes.EMOJI_ALIAS_UNICODE.keys())
    elif emoji_source == "slack_emoji":
        with open("./slack_emoji_list.txt", "r") as f:
            words = f.read().splitlines()
        return words
    raise Exception(f"Unsupported emoji type {emoji_source}")


def get_emoji_list_pairs() -> List[Tuple[str, str]]:
    return [
        (name[1:-1], label)
        for name, label in emoji.unicode_codes.EMOJI_ALIAS_UNICODE.items()
    ]


def overlapping_emoji_name(word: str, emoji_source: str = "uni_emoji") -> str:
    """ return an emoji based on overlap with emojis. remove the leading and training :"""
    emoji_names = get_emoji_list(emoji_source)
    overlapping_names = [x.strip() for x in emoji_names if word in x]
    if len(overlapping_names) == 0:
        return random_emoji_name(emoji_source)
    return random.choice(overlapping_names)[1:-1]


def random_emoji_name(emoji_source: str = "uni_emoji") -> str:
    """ return a random emoji. remove the leading and training :"""
    return random.choice(get_emoji_list(emoji_source))[1:-1]


def write_word(
    word,
    foreground_emoji: str,
    background_emoji: str,
    border_emoji: str = "",
    border_size: int = 1,
    emojize: bool = True,
) -> str:
    """ Convert the word into emojis """
    # leave 1 empty column at the beggining
    output_lines = ["0" for i in range(7)]

    # draw each word
    for char in word:
        current_matrix = letters_to_matrix.get(char.lower(), EMPTY_LETTER)
        # draw each line of this word
        for i in range(7):
            output_lines[i] = output_lines[i] + current_matrix[i] + "0"

    # merge the lines
    # add 1 empty line at the top and at the bottom
    # all lines should be the same length, add border
    char_length = len(output_lines[0])
    output_str = ""

    if border_emoji:
        for _ in range(border_size):
            output_str += "2" * (char_length + 2 * border_size) + "\n"

    if border_emoji:
        output_str += "2" * border_size + "0" * char_length + "2" * border_size + "\n"
    else:
        output_str += "0" * char_length + "\n"

    for l in output_lines:
        if border_emoji:
            output_str += ("2" * border_size) + l + ("2" * border_size) + "\n"
        else:
            output_str += l + "\n"

    if border_emoji:
        output_str += "2" * border_size + "0" * char_length + "2" * border_size + "\n"
    else:
        output_str += "0" * char_length + "\n"

    if border_emoji:
        for _ in range(border_size):
            output_str += "2" * (char_length + 2 * border_size) + "\n"

    output_str = output_str.translate(
        str.maketrans(
            {
                "0": f":{background_emoji}:",
                "1": f":{foreground_emoji}:",
                "2": f":{border_emoji}:",
            }
        )
    )
    if emojize:
        return emoji.emojize(output_str, use_aliases=True)
    else:
        return output_str
    return output_str


def write_emoji_word(
    word: str,
    foreground: str,
    random_foreground: bool,
    suggested_foreground: bool,
    background: str,
    random_background: bool,
    suggested_background: bool,
    border: bool,
    border_emoji: str,
    border_size: int,
    random_border: bool,
    emojize: bool,
    emoji_source: str,
) -> str:
    """ Draw the given word using emojis. Each letter is a 5x7 emoji matrix. """
    if random_background:
        background = random_emoji_name(emoji_source)

    if suggested_background:
        background = overlapping_emoji_name(word, emoji_source=emoji_source)

    if random_foreground:
        foreground = random_emoji_name(emoji_source)

    if suggested_foreground:
        foreground = overlapping_emoji_name(word, emoji_source=emoji_source)

    if random_border:
        border_emoji = random_emoji_name(emoji_source)

    if not border:
        border_emoji = ""

    return write_word(
        word, foreground, background, border_emoji, border_size, emojize=emojize
    )


def default_emoji_params() -> Dict:
    """ returns dictionary of the default parameters """
    return {
        "foreground": "thumbs_up",
        "random_foreground": False,
        "suggested_foreground": False,
        "background": "white_large_square",
        "random_background": False,
        "suggested_background": False,
        "border": False,
        "border_emoji": "fire",
        "random_border": False,
        "border_size": 1,
        "emojize": True,
        "emoji_source": "uni_emoji",
    }


def print_examples() -> None:
    """ Print some examples to stdout """

    print("Emoji writter allows you to write words using emojis")
    print()
    print(
        "python emoji_writer.py --word hello --foreground alien --background bright_button"
    )
    print(
        write_emoji_word(
            "hello",
            "alien",
            False,
            False,
            "bright_button",
            False,
            False,
            False,
            "",
            0,
            True,
            "uni_emoji",
        )
    )
    return "a"
