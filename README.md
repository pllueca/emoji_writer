# Emoji Writer
Python package to write words using emojis

## Instalation
`emoji_writer` can be installed from pip:

```
pip install emoji_writer
```

or cloned from github:
```
git clone
https://github.com/pllueca/emoji_writer
```

to install and run the tests locally
```
pip install -r requirements.txt
pytest test
```

Also can use containerized:

Build the container
```
make build
```

Run the test inside the container
```
make test
```

To build the python package:
```
make buildpkg
```

## Usage (Python module)

```python
from emoji_writer import write_emoji_word
print(write_emoji_word("hello", foreground="✅", background="👽"))
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽
👽✅👽👽👽✅👽✅✅✅✅✅👽✅👽👽👽👽👽✅👽👽👽👽👽👽✅✅✅👽👽
👽✅👽👽👽✅👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽✅👽
👽✅👽👽👽✅👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽✅👽
👽✅✅✅✅✅👽✅✅✅✅👽👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽✅👽
👽✅👽👽👽✅👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽✅👽
👽✅👽👽👽✅👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽👽👽✅👽👽👽✅👽
👽✅👽👽👽✅👽✅✅✅✅✅👽✅✅✅✅✅👽✅✅✅✅✅👽👽✅✅✅👽👽
👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽

>>> print(write_emoji_word("hello", foreground="alien", background="thumbs_up"))
👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍
👍👽👍👍👍👽👍👽👽👽👽👽👍👽👍👍👍👍👍👽👍👍👍👍👍👍👽👽👽👍👍
👍👽👍👍👍👽👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👽👍
👍👽👍👍👍👽👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👽👍
👍👽👽👽👽👽👍👽👽👽👽👍👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👽👍
👍👽👍👍👍👽👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👽👍
👍👽👍👍👍👽👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👍👍👽👍👍👍👽👍
👍👽👍👍👍👽👍👽👽👽👽👽👍👽👽👽👽👽👍👽👽👽👽👽👍👍👽👽👽👍👍
👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍
```

## Usage (Scripts)


`python main.py write --word hello --foreground 👽 --background 🤤`

```
🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤
🤤👽🤤🤤🤤👽🤤👽👽👽👽👽🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤🤤👽👽👽🤤🤤
🤤👽🤤🤤🤤👽🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤👽🤤
🤤👽🤤🤤🤤👽🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤👽🤤
🤤👽👽👽👽👽🤤👽👽👽👽🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤👽🤤
🤤👽🤤🤤🤤👽🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤👽🤤
🤤👽🤤🤤🤤👽🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤🤤🤤👽🤤🤤🤤👽🤤
🤤👽🤤🤤🤤👽🤤👽👽👽👽👽🤤👽👽👽👽👽🤤👽👽👽👽👽🤤🤤👽👽👽🤤🤤
🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤
```

`python main.py write --word hello --foreground alien --background bright_button`

```
🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆
🔆👽🔆🔆🔆👽🔆👽👽👽👽👽🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆🔆👽👽👽🔆🔆
🔆👽🔆🔆🔆👽🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽👽👽👽👽🔆👽👽👽👽🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆🔆🔆👽🔆🔆🔆👽🔆
🔆👽🔆🔆🔆👽🔆👽👽👽👽👽🔆👽👽👽👽👽🔆👽👽👽👽👽🔆🔆👽👽👽🔆🔆
🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆
```

Also supports and optional border:

`python main.py write --word LGTM! --foreground brain --background "blue_circle" --border --border-size 2`

```
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
🔥🔥🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔥🔥
🔥🔥🔵🧠🔵🔵🔵🔵🔵🔵🧠🧠🧠🔵🔵🧠🧠🧠🧠🧠🔵🧠🔵🔵🔵🧠🔵🔵🧠🔵🔵🔥🔥
🔥🔥🔵🧠🔵🔵🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🧠🧠🔵🧠🧠🔵🔵🧠🔵🔵🔥🔥
🔥🔥🔵🧠🔵🔵🔵🔵🔵🧠🔵🔵🔵🔵🔵🔵🔵🧠🔵🔵🔵🧠🔵🧠🔵🧠🔵🔵🧠🔵🔵🔥🔥
🔥🔥🔵🧠🔵🔵🔵🔵🔵🧠🔵🔵🔵🔵🔵🔵🔵🧠🔵🔵🔵🧠🔵🧠🔵🧠🔵🔵🧠🔵🔵🔥🔥
🔥🔥🔵🧠🔵🔵🔵🔵🔵🧠🔵🔵🧠🧠🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🧠🔵🔵🔥🔥
🔥🔥🔵🧠🔵🔵🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🔵🔵🔥🔥
🔥🔥🔵🧠🧠🧠🧠🧠🔵🔵🧠🧠🧠🔵🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🔵🧠🔵🔵🧠🔵🔵🔥🔥
🔥🔥🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔥🔥
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
```	

If you are feeling lucky you can use random emojis (some of them are smaller and it breaks the shapes):

`python main.py write --word "random" --random-foreground --random-background`

```
🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤
🏤🧜🧜🧜🧜🏤🏤🏤🧜🧜🧜🏤🏤🧜🏤🏤🏤🧜🏤🧜🧜🧜🧜🏤🏤🏤🧜🧜🧜🏤🏤🧜🏤🏤🏤🧜🏤
🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🧜🏤🧜🧜🏤
🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🧜🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🧜🏤🧜🏤
🏤🧜🧜🧜🧜🏤🏤🧜🧜🧜🧜🧜🏤🧜🏤🧜🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🧜🏤🧜🏤
🏤🧜🏤🧜🏤🏤🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🧜🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤
🏤🧜🏤🏤🧜🏤🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤
🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🏤🏤🏤🧜🏤🧜🧜🧜🧜🏤🏤🏤🧜🧜🧜🏤🏤🧜🏤🏤🏤🧜🏤
🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤🏤
```
You can also let the program decide which emojis to use based on the input word!

`python main.py write --word party --suggested-background --suggested-foreground`

```
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
🎉🥳🥳🥳🥳🎉🎉🎉🥳🥳🥳🎉🎉🥳🥳🥳🥳🎉🎉🥳🥳🥳🥳🥳🎉🥳🎉🎉🎉🥳🎉
🎉🥳🎉🎉🎉🥳🎉🥳🎉🎉🎉🥳🎉🥳🎉🎉🎉🥳🎉🎉🎉🥳🎉🎉🎉🥳🎉🎉🎉🥳🎉
🎉🥳🎉🎉🎉🥳🎉🥳🎉🎉🎉🥳🎉🥳🎉🎉🎉🥳🎉🎉🎉🥳🎉🎉🎉🎉🥳🎉🥳🎉🎉
🎉🥳🥳🥳🥳🎉🎉🥳🥳🥳🥳🥳🎉🥳🥳🥳🥳🎉🎉🎉🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉
🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉🥳🎉🥳🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉
🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉🥳🎉🥳🎉🎉🥳🎉🎉🎉🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉
🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉🥳🎉🥳🎉🎉🎉🥳🎉🎉🎉🥳🎉🎉🎉🎉🎉🥳🎉🎉🎉
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
```

Letters can also be written in vertical:

`python main.py write --word hello --foreground fire --background white_large_square --border --border-emoji ATM_sign --vertical`

outputs
```
🏧🏧🏧🏧🏧🏧🏧🏧🏧
🏧⬜⬜⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥🔥🔥🔥🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜⬜⬜⬜⬜⬜⬜🏧
🏧⬜🔥🔥🔥🔥🔥⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥🔥🔥🔥⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥🔥🔥🔥🔥⬜🏧
🏧⬜⬜⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥🔥🔥🔥🔥⬜🏧
🏧⬜⬜⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥⬜⬜⬜⬜⬜🏧
🏧⬜🔥🔥🔥🔥🔥⬜🏧
🏧⬜⬜⬜⬜⬜⬜⬜🏧
🏧⬜⬜🔥🔥🔥⬜⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜🔥⬜⬜⬜🔥⬜🏧
🏧⬜⬜🔥🔥🔥⬜⬜🏧
🏧⬜⬜⬜⬜⬜⬜⬜🏧
🏧🏧🏧🏧🏧🏧🏧🏧🏧
```

You can print all the examples running `python main.py examples`

## TODO
Features that would be nice to implement:

* [x] Support for multiline output
* [x] Random emojis, choosing emojis based on input word
* [ ] Slack integration
* [ ] groups of emojis: flags, faces, foods... Make able to get a random one from a group
* [ ] list available emojis
* [x] serving emojis through an http api

