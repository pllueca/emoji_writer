from emoji_writer.letters import letters_to_matrix


def test_letters_length():
    for letter, matrix in letters_to_matrix.items():
        assert len(matrix) == 7, f"matrix for letter {letter} does not have 7 rows"
