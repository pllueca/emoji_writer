""" Python emoji writter.
write works in 7x5 grids, with emojis
"""
import random

import emoji
import click

# LETTER DEFINITIONS
A = [
    '01110',
    '10001',
    '10001',
    '11111',
    '10001',
    '10001',
    '10001',
]

B = [
    '11110',
    '10001',
    '10001',
    '11110',
    '10001',
    '10001',
    '11110',
]

C = [
    '01110',
    '10001',
    '10000',
    '10000',
    '10000',
    '10001',
    '01110',
]

D = [
    '11110',
    '10001',
    '10001',
    '10001',
    '10001',
    '10001',
    '11110',
]

E = [
    '11111',
    '10000',
    '10000',
    '11110',
    '10000',
    '10000',
    '11111',
]

F = [
    '11111',
    '10000',
    '10000',
    '11110',
    '10000',
    '10000',
    '10000',
]

G = [
    '01110',
    '10001',
    '10000',
    '10000',
    '10011',
    '10001',
    '01110',
]

H = [
    '10001',
    '10001',
    '10001',
    '11111',
    '10001',
    '10001',
    '10001',
]

I = [
    '01110',
    '00100',
    '00100',
    '00100',
    '00100',
    '00100',
    '01110',
]

J = [
    '00111',
    '00010',
    '00010',
    '00010',
    '00010',
    '10010',
    '01100',
]

K = [
    '10001',
    '10010',
    '10100',
    '11000',
    '10100',
    '10010',
    '10001',
]

L = [
    '10000',
    '10000',
    '10000',
    '10000',
    '10000',
    '10000',
    '11111',
]

M = [
    '10001',
    '11011',
    '10101',
    '10101',
    '10001',
    '10001',
    '10001',
]

N = [
    '10001',
    '10001',
    '11001',
    '10101',
    '10011',
    '10001',
    '10001',
]

O = [
    '01110',
    '10001',
    '10001',
    '10001',
    '10001',
    '10001',
    '01110',
]

P = [
    '11110',
    '10001',
    '10001',
    '11110',
    '10000',
    '10000',
    '10000',
]

Q = [
    '01110',
    '10001',
    '10001',
    '10001',
    '10101',
    '10010',
    '01101',
]

R = [
    '11110',
    '10001',
    '10001',
    '11110',
    '10100',
    '10010',
    '10001',
]

S = [
    '01111',
    '10000',
    '10000',
    '01110',
    '00001',
    '00001',
    '11110',
]

T = [
    '11111',
    '00100',
    '00100',
    '00100',
    '00100',
    '00100',
    '00100',
]

U = [
    '10001',
    '10001',
    '10001',
    '10001',
    '10001',
    '10001',
    '01110',
]

V = [
    '10001',
    '10001',
    '10001',
    '01010',
    '01010',
    '00100',
]

W = [
    '10001',
    '10001',
    '10101',
    '10101',
    '10101',
    '11011',
    '10001',
]

X = [
    '10001',
    '10001',
    '01010',
    '00100',
    '01010',
    '10001',
    '10001',
]

Y = [
    '10001',
    '10001',
    '01010',
    '00100',
    '00100',
    '00100',
    '00100',
]

Z = [
    '11111',
    '00001',
    '00010',
    '00100',
    '01000',
    '10000',
    '11111',
]

EMPTY_LETTER = [
    '11111',
    '11111',
    '11111',
    '11111',
    '11111',
    '11111',
    '11111',
]

SPACE = [
    '000',
    '000',
    '000',
    '000',
    '000',
    '000',
    '000',
]

PIPE = [
    '010',
    '010',
    '010',
    '010',
    '010',
    '010',
    '010',
]

EXCLAMATION_MARK = [
    '010',
    '010',
    '010',
    '010',
    '010',
    '000',
    '010',
]
letters_to_matrix = {
    'a': A,
    'b': B,
    'c': C,
    'd': D,
    'e': E,
    'f': F,
    'g': G,
    'h': H,
    'i': I,
    'j': J,
    'k': K,
    'l': L,
    'm': M,
    'n': N,
    'o': O,
    'p': P,
    'r': R,
    's': S,
    't': T,
    'u': U,
    'v': V,
    'w': W,
    'x': X,
    'y': Y,
    'z': Z,
    ' ': SPACE,
    '|': PIPE,
    '!': EXCLAMATION_MARK,
}


def random_emoji_name() -> str:
  """ return a random emoji. remove the leading and training :"""
  return random.choice(list(emoji.unicode_codes.EMOJI_ALIAS_UNICODE.keys()))[1:-1]


@click.command()
@click.option('--word', help='word to write', required=True)
@click.option('--foreground', help='foreground emoji', default='thumbs_up')
@click.option('--random-foreground', default=False, is_flag=True)
@click.option('--background', help='background emoji', default='white_large_square')
@click.option('--random-background', default=False, is_flag=True)
@click.option(
    '--border', default=False, help='If true, draw a border using border-emoji', is_flag=True)
@click.option('--border-emoji', default='fire')
@click.option('--border-size', type=int, default=1)
@click.option('--emojize/--no-emojize', default=True)
def write_emoji_word(
    word: str,
    foreground: str,
    random_foreground: bool,
    background: str,
    random_background: bool,
    border: bool,
    border_emoji: str,
    border_size: int,
    emojize: bool,
):
  """ Draw the given word using emojis. Each letter is a 5x7 emoji matrix. """

  if random_background:
    background = random_emoji_name()

  if random_foreground:
    foreground = random_emoji_name()

  # leave 1 empty column at the beggining
  output_lines = ['0' for i in range(7)]

  # draw each word
  for char in word:
    current_matrix = letters_to_matrix.get(char.lower(), EMPTY_LETTER)
    # draw each line of this word
    for i in range(7):
      output_lines[i] = output_lines[i] + current_matrix[i] + '0'

  # merge the lines
  # add 1 empty line at the top and at the bottom
  # all lines should be the same length, add border
  char_length = len(output_lines[0])
  output_str = ''

  if border:
    for _ in range(border_size):
      output_str += '2' * (char_length + 2 * border_size) + '\n'

  if border:
    output_str += '2' * border_size + '0' * char_length + '2' * border_size + '\n'
  else:
    output_str += '0' * char_length + '\n'

  for l in output_lines:
    if border:
      output_str += ('2' * border_size) + l + ('2' * border_size) + '\n'
    else:
      output_str += l + '\n'

  if border:
    output_str += '2' * border_size + '0' * char_length + '2' * border_size + '\n'
  else:
    output_str += '0' * char_length + '\n'

  if border:
    for _ in range(border_size):
      output_str += '2' * (char_length + 2 * border_size) + '\n'

  output_str = output_str.translate(
      str.maketrans({
          '0': f':{background}:',
          '1': f':{foreground}:',
          '2': f':{border_emoji}:',
      }))

  if emojize:
    print(emoji.emojize(output_str, use_aliases=True))
  else:
    print(output_str)


if __name__ == '__main__':
  write_emoji_word()  # pylint: disable=no-value-for-parameter
