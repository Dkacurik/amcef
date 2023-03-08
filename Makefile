debug:
	docker-compose -f docker-compose.yml -f docker-compose.debug.yml up

run:
	docker-compose -f docker-compose.yml up

build:
	docker-compose build

flake8:
	flake8 --config .flake8
