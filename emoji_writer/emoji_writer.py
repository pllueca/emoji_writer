""" Python emoji writter.
write works in 7x5 grids, with emojis
"""
import random
import string
import sys
from typing import Dict, List, Optional, Tuple

import emoji

from .groups import emoji_groups, get_emoji_dict, get_emoji_list_names, is_emoji
from .letters import EMPTY_LETTER, letters_to_matrix

# letters are drawn in a 5x7 matrix
LETTER_WIDTH: int = 5
LETTER_HEIGHT: int = 7

BG_CHAR: str = "0"
FG_CHAR: str = "1"
BORDER_CHAR: str = "2"


def overlapping_emoji_name(word: str, emoji_source: str = "short") -> str:
    """return an emoji based on overlap with emojis. remove the leading and training :"""
    emoji_names = get_emoji_list_names(emoji_source)
    overlapping_names = [x.strip() for x in emoji_names if word in x]
    if len(overlapping_names) == 0:
        return random_emoji_name(emoji_source)
    return random.choice(overlapping_names)[1:-1]


def random_emoji_name(emoji_source: str = "short") -> str:
    """return a random emoji. remove the leading and training :"""
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
    vertical: bool = False,
) -> str:
    """Convert the word into emojis.
    if first_line draw border on top
    if last_line draw border on bottom
    if vertical write 1 emoji per column
    """

    use_border = border_emoji != "" and border_size > 0

    if not is_emoji(foreground_emoji):
        foreground_emoji = emoji.emojize(f":{foreground_emoji}:")

    if not is_emoji(background_emoji):
        background_emoji = emoji.emojize(f":{background_emoji}:")

    if not is_emoji(border_emoji):
        border_emoji = emoji.emojize(f":{border_emoji}:")

    if not emojize:
        background_emoji = emoji.UNICODE_EMOJI_ENGLISH[background_emoji]
        foreground_emoji = emoji.UNICODE_EMOJI_ENGLISH[foreground_emoji]
        try:
            border_emoji = emoji.UNICODE_EMOJI_ENGLISH[border_emoji]
        except KeyError:
            # if not using border is fine to error here
            if use_border:
                raise

    if vertical:
        output_str = write_word_vertical(
            word,
            use_border,
            border_size,
        )
    else:
        output_str = write_word_horizontal(
            word,
            use_border,
            border_size,
            first_line,
            last_line,
        )

    output_str = output_str.translate(
        str.maketrans(
            {
                "0": background_emoji,
                "1": foreground_emoji,
                "2": border_emoji,
            }
        )
    )
    return output_str


def write_word_vertical(
    word,
    use_border: bool,
    border_size: int = 1,
) -> str:
    """Draw a vertical word. EAch letter is in the same column"""
    text_width: int = LETTER_WIDTH + 2
    if use_border:
        text_width += 2 * border_size

    output_lines: List[str] = []

    def add_blank_line():
        if use_border:
            output_lines.append(
                BORDER_CHAR * border_size
                + BG_CHAR * (LETTER_WIDTH + 2)
                + BORDER_CHAR * border_size
            )
        else:
            output_lines.append("".join(BG_CHAR for _ in range(text_width)))

    def add_border_line():
        output_lines.append(BORDER_CHAR * text_width)

    # write top border
    if use_border:
        for _ in range(border_size):
            add_border_line()
    add_blank_line()

    # Write letters
    # TODO: handle spaces and non letter characters
    for letter in word:
        current_letter_matrix = letters_to_matrix.get(letter.lower(), EMPTY_LETTER)
        # for each row in the letter
        for letter_line in current_letter_matrix:
            # 0letter0
            # line without the border
            line = BG_CHAR + letter_line + BG_CHAR
            if use_border:
                line = BORDER_CHAR * border_size + line + BORDER_CHAR * border_size
            output_lines.append(line)
        add_blank_line()

    # write bottom border
    if use_border:
        for _ in range(border_size):
            add_border_line()

    output_str: str = "\n".join(output_lines) + "\n"
    return output_str


def write_word_horizontal(
    word,
    use_border: bool,
    border_size: int = 1,
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

    if use_border and first_line:
        for _ in range(border_size):
            output_str += "2" * (char_length + 2 * border_size) + "\n"

    if use_border:
        output_str += "2" * border_size + "0" * char_length + "2" * border_size + "\n"
    else:
        output_str += "0" * char_length + "\n"

    for l in output_lines:
        if use_border:
            output_str += ("2" * border_size) + l + ("2" * border_size) + "\n"
        else:
            output_str += l + "\n"

    if last_line:
        if use_border:
            output_str += (
                "2" * border_size + "0" * char_length + "2" * border_size + "\n"
            )
        else:
            output_str += "0" * char_length

        if use_border:
            for border_idx in range(border_size):
                output_str += "2" * (char_length + 2 * border_size)
                # dont but \n at the end
                if border_idx != border_size - 1:
                    output_str += "\n"
    return output_str


def write_emoji_word(
    word: str,
    foreground: Optional[str] = None,
    random_foreground: bool = False,
    suggested_foreground: Optional[bool] = None,
    background: Optional[str] = None,
    random_background: bool = False,
    suggested_background: bool = False,
    border: bool = False,
    border_emoji: Optional[str] = None,
    border_size: int = 1,
    random_border: bool = False,
    emojize: bool = True,
    emoji_group_foreground: str = "short",
    emoji_group_background: str = "short",
    emoji_group_border: str = "short",
    vertical: bool = False,
) -> str:
    """Draw the given word using emojis. Each letter is a 5x7 emoji matrix."""
    if random_background:
        background = random_emoji_name(emoji_group_background)

    if suggested_background:
        background = overlapping_emoji_name(word, emoji_group_background)

    if random_foreground:
        foreground = random_emoji_name(emoji_group_foreground)

    if suggested_foreground:
        foreground = overlapping_emoji_name(word, emoji_group_foreground)

    if random_border:
        border_emoji = random_emoji_name()

    if not border:
        border_emoji = ""

    lines = word.split("\n")
    if len(lines) == 1:
        return write_word(
            word,
            foreground,
            background,
            border_emoji,
            border_size,
            emojize=emojize,
            vertical=vertical,
        )
    if vertical:
        raise ValueError("Vertical output not supported for multiline inputs")
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
    """returns dictionary of the default parameters"""
    return {
        "foreground": "👍",  # thumbs_up
        "random_foreground": False,
        "suggested_foreground": False,
        "background": "⬜",
        "random_background": False,
        "suggested_background": False,
        "border": False,
        "border_emoji": "🔥",
        "random_border": False,
        "border_size": 1,
        "emojize": True,
        "vertical": False,
    }


def print_examples() -> None:
    """Print some examples to stdout"""

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
        )
    )
    print()
    print(
        "python main.py write --word hello --foreground fire --background white_large_square"
        " --border --border-emoji ATM_sign"
        " --vertical"
    )
    # "white_large_square"# , "ATM_sign"
    print(
        write_emoji_word(
            "hello",
            foreground="fire",
            random_foreground=False,
            suggested_foreground=False,
            background="white_large_square",
            random_background=False,
            suggested_background=False,
            border=True,
            border_emoji="ATM_sign",
            border_size=1,
            random_border=False,
            emojize=True,
            vertical=True,
        )
    )


def list_emojis(group: Optional[str] = None) -> None:
    """list the available emojis"""
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
