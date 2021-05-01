mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

build:
	docker build . --tag emoji_writer:writer
build_debug:
	docker build . --tag emoji_writer --build-arg debug=true

build_server: 
	docker build . --tag emoji_writer:server --build-arg mode=server

test: build
	docker run --rm emoji_writer:writer pytest test

# run development server. mounts app.py
runserver: build_server
	docker run -p 8000:8000 -v $(mkfile_dir)app.py:/opt/app.py --rm -it emoji_writer:server \
		uvicorn app:app --reload --host 0.0.0.0
		


itest: build_debug
	docker run --rm -it emoji_writer pytest test -s -v

ipy: build
	docker run --rm -it emoji_writer python

bash: build
	docker run --rm -it emoji_writer bash

fmt:
	black .
	isort .

