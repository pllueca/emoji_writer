""" Groups of emojis """
import os
from pathlib import Path
from functools import cache
from typing import Dict, List, Tuple


DATA_PATH= Path(__file__) / '..' / 'data'
EMOJI_LIST_PATH = DATA_PATH / 'data-ordered-emoji.json'
import ipdb
ipdb.set_trace()
if not EMOJI_LIST_PATH.is_file():
    raise Exception

with EMOJI_LIST_PATH.open('r') as f:
    EMOJI_LIST = json.load(f)


@cache
def get_emoji_list_names(emoji_source: str) -> list:
    """ get list of emoji name based on specified type """
    if emoji_source not in emoji_groups:
        raise KeyError(f"Unsupported emoji group {emoji_source}")
    return emoji_groups[emoji_source]


@cache
def get_emoji_list_pairs() -> List[Tuple[str, str]]:
    return [
        (name[1:-1], label)
        for name, label in emoji.unicode_codes.EMOJI_ALIAS_UNICODE_ENGLISH.items()
    ]


@cache
def get_emoji_dict() -> Dict[str, str]:
    return {
        name[1:-1]: label
        for name, label in emoji.unicode_codes.EMOJI_ALIAS_UNICODE_ENGLISH.items()
    }


# emojis representing a flag

emoji_groups: Dict[str, List[str]] = {
    "flags": FLAGS,
    "short": short_emojis,
    "medium": medium_emojis,
    "long": long_emojis,
    "all": all_emojis,
    "slack": slack_emojis,
}
