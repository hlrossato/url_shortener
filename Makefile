# Docker services
PROJECT_PATH=/shortener/shortener
PROJECT_NAME=shortener
APP_ALIAS=shortener_web
DB_ALIAS=shortener_db


# Aliases
docker-down: docker-compose-down
docker-stop: docker-compose-stop
docker-ssh: docker-exec-ssh
docker-start: docker-compose-up
docker-build: docker-compose-build
docker-tests: docker-compose-build django-migrations django-migrate tests
docker-test: docker-compose-build django-migrations django-migrate test
docker-tests-with-coverage: docker-compose-build django-migrations django-migrate tests-cov

docker-compose-up:
	@echo "Starting Docker..."
	@docker-compose up

docker-start-pdb:
	@docker-compose run --service-ports app

docker-compose-build:
	@echo "Build docker images..."
	@docker-compose build

docker-compose-down:
	@echo "Stopping and putting containers down..."
	@docker-compose down --remove-orphans

docker-compose-stop:
	@echo "Stopping Docker..."
	@docker-compose stop

docker-exec-ssh:
	@echo "Entering bash..."
	@docker exec -it $(APP_ALIAS) /bin/bash

django-createsuperuser:
	@echo "Creating Django Superuser"
	@docker-compose run --workdir=$(PROJECT_PATH) app python manage.py createsuperuser

django-migrations:
	@docker-compose run --workdir=$(PROJECT_PATH) app python manage.py makemigrations

django-migrate:
	@docker-compose run --workdir=$(PROJECT_PATH) app python manage.py migrate

tests:
	@echo "Starting tests..."
	@docker-compose run --workdir=$(PROJECT_PATH) app pytest -v $(ARGS)

test:
	@echo "Starting test $(TEST)"
	@docker-compose run --workdir=$(PROJECT_PATH) app pytest -v $(TEST) $(ARGS)

tests-cov:
	@echo "Starting tests with coverage..."
	@docker-compose run --workdir=$(PROJECT_PATH) app pytest -v --cov --cov-report html $(ARGS)

django-shell:
	@echo "Starting Django shell.."
	@docker-compose run --workdir=$(PROJECT_PATH) app python manage.py shell_plus

django-startapp:
	@echo "Starting app $(APPNAME)"
	@docker-compose run --workdir=$(PROJECT_PATH) app django-admin startapp $(APPNAME)
