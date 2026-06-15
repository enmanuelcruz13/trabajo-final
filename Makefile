.PHONY: build up shell logs stop

build:
	docker-compose build

up:
	docker-compose up -d --remove-orphans

shell:
	docker-compose exec web bash

logs:
	docker-compose logs -f

stop:
	docker-compose down
