mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

build:
	docker build . --tag emoji_writer:writer -f dockerfiles/Dockerfile
build_debug:
	docker build . --tag emoji_writer:writer --build-arg debug=true -f dockerfiles/Dockerfile


test: build
	docker run --rm emoji_writer:writer pytest test


itest: build_debug
	docker run --rm -it emoji_writer:writer pytest test -s -v

ipy: build
	docker run --rm -it emoji_writer:writer python

bash: build
	docker run --rm -it emoji_writer:writer bash

examples: build
	docker run --rm emoji_writer:writer python main.py examples

fmt:
	black emoji_writer/ scripts/
	isort emoji_writer/ 

buildpkg:
	python3 -m build

pushpkg: buildpkg
	twine upload dist/*

testpkg:
	docker build -f dockerfiles/Dockerfile.test_package --tag emoji_writer:pkg-test .
	docker run --rm emoji_writer:pkg-test

