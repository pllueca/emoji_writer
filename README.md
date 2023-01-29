# Emoji Writer
Python package to write words using emojis

## Setup

```
pip install -r requirements.txt
```

to run the tests
```
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
 python3 -m build
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
push:
	docker tag plluecaweb:dev registry.digitalocean.com/pllueca-web/plluecaweb:latest
	docker push registry.digitalocean.com/pllueca-web/plluecaweb:latest
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

## Usage (server)
The file `app.py` implements an HTTP webserver with an endpoint to generate emoji words. It can be ran with `make runserver`. It runs inside a docker container that exposes port 8000.

Endpoints:

* `GET /`
* `GET /{word}?OPTIONS`, e.g.: /lgtm?foreground=%F0%9F%92%85&background=%F0%9F%A6%AC`


## TODO
Features that would be nice to implement:

* [x] Support for multiline output
* [x] Random emojis, choosing emojis based on input word
* [ ] Slack integration
* [ ] groups of emojis: flags, faces, foods... Make able to get a random one from a group
* [ ] list available emojis
* [x] serving emojis through an http api

