from emoji_writer.groups import FLAGS, emoji_groups


def test_flag_group():
    assert "flags" in emoji_groups
    flags = emoji_groups["flags"]
    assert flags == FLAGS
