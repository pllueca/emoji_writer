mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

build:
	docker build . --tag emoji_writer:writer
build_debug:
	docker build . --tag emoji_writer:writer --build-arg debug=true


test: build
	docker run --rm emoji_writer:writer pytest test

buildserver: 
	docker build . --tag emoji_writer:server -f Dockerfile.server

# run development server. mounts app.py
runserver: build_server
	docker run -p 8000:8000 -v $(mkfile_dir)app.py:/opt/app.py --rm -it emoji_writer:server
		
pushserver:
	docker tag emoji_writer:server registry.digitalocean.com/pllueca-web/plluecaweb:server-latest
	docker push registry.digitalocean.com/pllueca-web/plluecaweb:server-latest


itest: build_debug
	docker run --rm -it emoji_writer:writer pytest test -s -v

ipy: build
	docker run --rm -it emoji_writer:writer python

bash: build
	docker run --rm -it emoji_writer:writer bash

examples: build
	docker run --rm emoji_writer:writer python main.py examples

fmt:
	black .
	isort .

