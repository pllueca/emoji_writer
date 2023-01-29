from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from emoji_writer import (
    default_emoji_params,
    list_emojis,
    print_examples,
    write_emoji_word,
)

app = FastAPI()

# base template
base_html = """<!DOCTYPE html>
<html>
<body>

{emoji_word}

</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home():
    emoji_word = write_emoji_word(
        "hola", foreground="thumbs_up", random_background=True
    )
    emoji_word = emoji_word.replace("\n", "<br>")
    return base_html.format(emoji_word=emoji_word)


@app.get("/{word}", response_class=HTMLResponse)
def write_word(
    word: str,
    foreground: Optional[str] = "",
    random_foreground: bool = False,
    background: str = "",
    random_background: bool = False,
    border: bool = False,
    border_emoji: str = "",
    random_border: bool = False,
    border_size: int = 1,
):
    default_params = default_emoji_params()
    if not random_foreground and not foreground:
        foreground = default_params["foreground"]

    if not random_background and not background:
        background = default_params["background"]

    if not random_border and not border_emoji:
        border_emoji = default_params["border_emoji"]

    emoji_word = write_emoji_word(
        word,
        foreground=foreground,
        random_foreground=random_foreground,
        background=background,
        random_background=random_background,
        border=border,
        border_emoji=border_emoji,
        random_border=random_border,
        border_size=border_size,
    )
    emoji_word = emoji_word.replace("\n", "<br>")
    return base_html.format(emoji_word=emoji_word)
