""" Python emoji writter.
write works in 7x5 grids, with emojis
"""
from typing import Dict, List, Tuple, Optional
import sys
import random

import emoji

from .letters import letters_to_matrix, EMPTY_LETTER
from .groups import get_emoji_list_names, get_emoji_dict, emoji_groups


def overlapping_emoji_name(word: str, emoji_source: str = "uni_emoji") -> str:
    """ return an emoji based on overlap with emojis. remove the leading and training :"""
    emoji_names = get_emoji_list_names(emoji_source)
    overlapping_names = [x.strip() for x in emoji_names if word in x]
    if len(overlapping_names) == 0:
        return random_emoji_name(emoji_source)
    return random.choice(overlapping_names)[1:-1]


def random_emoji_name(emoji_source: str = "uni_emoji") -> str:
    """ return a random emoji. remove the leading and training :"""
    return random.choice(get_emoji_list_names(emoji_source))[1:-1]


def write_word(
    word,
    foreground_emoji: str,
    background_emoji: str,
    border_emoji: str = "",
    border_size: int = 1,
    emojize: bool = True,
    first_line: bool = True,
    last_line: bool = True,
) -> str:
    """Convert the word into emojis.
    if first_line draw border on top
    if last_line draw border on bottom
    """
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

    if border_emoji and first_line:
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

    if last_line:
        if border_emoji:
            output_str += (
                "2" * border_size + "0" * char_length + "2" * border_size + "\n"
            )
        else:
            output_str += "0" * char_length

        if border_emoji:
            for border_idx in range(border_size):
                output_str += "2" * (char_length + 2 * border_size)
                # dont but \n at the end
                if border_idx != border_size - 1:
                    output_str += "\n"

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

    lines = word.split("\n")
    if len(lines) == 1:
        return write_word(
            word, foreground, background, border_emoji, border_size, emojize=emojize
        )
    # pad all lines up to longest line
    line_length = lambda l: sum([3 if c == " " else 5 for c in l])
    longest_line_length = max(line_length(l) for l in lines)
    output_word = ""
    # TODO add spaces to lines to make them the same length
    for line_idx, line in enumerate(lines):
        first_line = line_idx == 0
        last_line = line_idx == len(lines) - 1
        pad = longest_line_length - line_length(line)
        long_pads = pad // 5
        pad %= 5
        med_pads = pad // 3
        short_pads = pad % 3

        # TODO pad inteligently here
        padded_line = line + "@" * long_pads + "%" * med_pads + "#" * short_pads
        output_word += write_word(
            padded_line,
            foreground,
            background,
            border_emoji,
            border_size,
            emojize,
            first_line,
            last_line,
        )
    return output_word


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
        "python main.py write --word hello --foreground alien --background bright_button"
    )
    print(
        write_emoji_word(
            "hello",
            foreground="alien",
            random_foreground=False,
            suggested_foreground=False,
            background="bright_button",
            random_background=False,
            suggested_background=False,
            border=False,
            border_emoji="",
            border_size=0,
            random_border=False,
            emojize=True,
            emoji_source="uni_emoji",
        )
    )

    print()
    print("python main.py --word party --suggested-background --suggested-foreground")
    print(
        write_emoji_word(
            "party",
            foreground="",
            random_foreground=False,
            suggested_foreground=True,
            background="",
            random_background=False,
            suggested_background=True,
            border=False,
            border_emoji="",
            border_size=0,
            random_border=False,
            emojize=True,
            emoji_source="uni_emoji",
        )
    )


def list_emojis(group: Optional[str] = None) -> None:
    """ list the available emojis """
    all_emojis = get_emoji_dict()
    if group is not None:
        if group not in emoji_groups:
            print(
                f"Group of emojis {group} not available. "
                f"Avaliable groups: {list(emoji_groups.keys())}"
            )
            return
        emojis_to_list = emoji_groups[group]
        print(f"Available emojis for group <{group}>:")
    else:
        print("Available emojis:")
        emojis_to_list = [t for t in all_emojis]

    for emoji_str in emojis_to_list:
        emoji = all_emojis[emoji_str]
        print(f"{emoji_str}: {emoji}")
