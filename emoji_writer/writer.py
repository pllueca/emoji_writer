""" Emoji writer logic """

from typing import Dict, List, Optional

from .letters import EMPTY_LETTER, letters_to_matrix


class Writer:

    LETTER_HEIGHT: int = 7  # size of the letters.
    TOP_PADDING: int = 1  # space between the top border and letters
    BOTTOM_PADDING: int = 1  # space between the bottom border and letters
    LEFT_PADDING: int = 1
    RIGHT_PADDING: int = 1
    LETTER_DISTANCE: int = 1

    def __init__(
        self,
        foreground_emoji: str,
        background_emoji: str,
        border_emoji: Optional[str] = None,
        border_size: int = 1,
        vertical: bool = False,
    ):
        self.foreground_emoji: str = foreground_emoji
        self.background_emoji: str = background_emoji
        self.border_emoji: Optional[str] = border_emoji
        self.border_size: int = border_size
        self.vertical: bool = vertical

    @property
    def config(self) -> Dict:
        cfg = {
            "foreground": self.foreground_emoji,
            "background": self.background_emoji,
            "has_border": self.has_border,
        }
        if self.has_border:
            cfg.update(
                {
                    "border_size": self.border_size,
                    "border": self.border_emoji,
                }
            )
        return cfg

    @property
    def has_border(self) -> bool:
        return self.border_emoji is not None and self.border_size > 0

    def write_line(
        self, word: str, first_line: bool = True, last_line: bool = True
    ) -> str:
        if self.vertical:
            pass
        else:
            return self._write_line_horizontal(word, first_line, last_line)

    def _write_line_horizontal(
        self, word: str, first_line: bool, last_line: bool
    ) -> str:
        # leave 1 empty column at the beggining

        height = self.LETTER_HEIGHT + self.BOTTOM_PADDING + self.TOP_PADDING

        # draw above word: top border and padding
        if self.has_border:
            if first_line:
                height += self.border_size
            if last_line:
                height += self.border_size

        output_lines = ["" for i in range(height)]
        # draw intial space and border
        if self.has_border:
            for _ in range(self.border_size):
                for line_idx in range(height):
                    output_lines[line_idx] += self.border_emoji

        for _ in range(self.LEFT_PADDING):
            if self.has_border:
                row_idx = 0
                for _ in range(self.border_size):
                    output_lines[row_idx] += self.border_emoji
                    row_idx += 1
                for _ in range(height - 2 * self.border_size):
                    output_lines[row_idx] += self.background_emoji
                    row_idx += 1
                for _ in range(self.border_size):
                    output_lines[row_idx] += self.border_emoji
                    row_idx += 1

            else:
                for line_idx in range(height):
                    output_lines[line_idx] += self.background_emoji

        # draw word characters
        for i, char in enumerate(word):
            current_matrix = letters_to_matrix.get(char.lower(), EMPTY_LETTER)
            columns = len(current_matrix[0])
            for columns_idx in range(columns):
                row_idx = 0
                if self.has_border:
                    for _ in range(self.border_size):
                        output_lines[row_idx] += self.border_emoji
                        row_idx += 1

                for _ in range(self.TOP_PADDING):
                    output_lines[row_idx] += self.background_emoji
                    row_idx += 1

                for letter_row in range(self.LETTER_HEIGHT):
                    current_emoji = (
                        self.foreground_emoji
                        if current_matrix[letter_row][columns_idx] == "1"
                        else self.background_emoji
                    )
                    output_lines[row_idx] += current_emoji
                    row_idx += 1

                for _ in range(self.BOTTOM_PADDING):
                    output_lines[row_idx] += self.background_emoji
                    row_idx += 1

                if self.has_border:
                    for _ in range(self.border_size):
                        output_lines[row_idx] += self.border_emoji
                        row_idx += 1

            # draw space between letters if not the last letter
            if i != len(word) - 1:
                for _ in range(self.LETTER_DISTANCE):
                    if self.has_border:
                        row_idx = 0
                        for _ in range(self.border_size):
                            output_lines[row_idx] += self.border_emoji
                            row_idx += 1
                        for _ in range(height - 2 * self.border_size):
                            output_lines[row_idx] += self.background_emoji
                            row_idx += 1
                        for _ in range(self.border_size):
                            output_lines[row_idx] += self.border_emoji
                            row_idx += 1

                    else:
                        for line_idx in range(height):
                            output_lines[line_idx] += self.background_emoji

        # each letter is drawn now
        # draw right padding and border
        for _ in range(self.RIGHT_PADDING):
            if self.has_border:
                row_idx = 0
                for _ in range(self.border_size):
                    output_lines[row_idx] += self.border_emoji
                    row_idx += 1
                for _ in range(height - 2 * self.border_size):
                    output_lines[row_idx] += self.background_emoji
                    row_idx += 1
                for _ in range(self.border_size):
                    output_lines[row_idx] += self.border_emoji
                    row_idx += 1

            else:
                for line_idx in range(height):
                    output_lines[line_idx] += self.background_emoji

        if self.has_border:
            for _ in range(self.border_size):
                for line_idx in range(height):
                    output_lines[line_idx] += self.border_emoji

        return "\n".join(output_lines)
