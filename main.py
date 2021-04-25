import click
from emoji_writer import write_emoji_word, get_emoji_dict, emoji_groups, print_examples


@click.group()
def cli():
    pass


@cli.command()
@click.option("-w", "--word", help="word to write", required=True)
@click.option("-fg", "--foreground", help="foreground emoji", default="thumbs_up")
@click.option("-rf", "--random-foreground", default=False, is_flag=True)
@click.option("--suggested-foreground", default=False, is_flag=True)
@click.option(
    "-bg", "--background", help="background emoji", default="white_large_square"
)
@click.option("-rb", "--random-background", default=False, is_flag=True)
@click.option("--suggested-background", default=False, is_flag=True)
@click.option(
    "-b",
    "--border",
    default=False,
    help="If true, draw a border using border-emoji",
    is_flag=True,
)
@click.option("--border-emoji", default="fire")
@click.option("--border-size", type=int, default=1)
@click.option("-rbo", "--random-border", default=False, is_flag=True)
@click.option("--emojize/--no-emojize", default=True)
@click.option("--emoji-source", default="uni_emoji")
def write(
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
) -> None:
    """Emoji writter allows you to write words using emojis

    Examples

    python main.py --word hello --foreground alien --background bright_button
    python main.py --word LGTM! --foreground brain --background "blue_circle" --border --border-size 2
    python main.py --word "random" -rf -rb
    python main.py --word party --suggested-background --suggested-foreground"""
    print(
        write_emoji_word(
            word=word,
            foreground=foreground,
            random_foreground=random_foreground,
            suggested_foreground=suggested_foreground,
            background=background,
            random_background=random_background,
            suggested_background=suggested_background,
            border=border,
            border_emoji=border_emoji,
            random_border=random_border,
            border_size=border_size,
            emojize=emojize,
            emoji_source=emoji_source,
        )
    )


@cli.command()
@click.argument("group", required=False)
def list(group=None):
    """ Prints a list of the available emojis """

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
        emojis_to_list = [t[0] for t in all_emojis]

    for emoji_str in emojis_to_list:
        emoji = all_emojis[emoji_str]
        print(f"{emoji_str}: {emoji}")


@cli.command()
def examples():
    """ print some examples """
    print_examples()


if __name__ == "__main__":
    cli()
