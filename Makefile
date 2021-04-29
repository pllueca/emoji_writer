build:
	docker build . --tag emoji_writer
build_debug:
	docker build . --tag emoji_writer --build-arg debug=true

test: build
	docker run --rm emoji_writer pytest test

itest: build_debug
	docker run --rm -it emoji_writer pytest test -s -v

ipy: build
	docker run --rm -it emoji_writer python

bash: build
	docker run --rm -it emoji_writer bash

fmt:
	black .
	isort .

