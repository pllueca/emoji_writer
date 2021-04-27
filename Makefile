build:
	docker build . --tag emoji_writer

test: build
	docker run --rm emoji_writer pytest test

itest: build
	docker run --rm -it emoji_writer pytest test -s -v

ipy: build
	docker run --rm -it emoji_writer python
bash: build
	docker run --rm -it emoji_writer bash


