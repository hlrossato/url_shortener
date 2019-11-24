# URL Shortener

**Disclaimer:** _This project is intend for test purposes and is not ready for production._

## The task
You are asked to create a URL shortening service. This system should:

## Functionality
1. Given a long url, returns a short code for it.
2. Given a short url, returns the long url if it exists or not found.

## Approach
For this project I'm using, mainly, Django and Django-Crispy-Forms. Although there are more dependencies installed, those are not directly linked to the project.

## How to run the project
The project is built using `Docker` and `Docker-compose` and all the commands needed to run everything on the project can be found in the `Makefile`.

In order to run the project some steps must be followed. Please find the steps and explanation to those below:

- To build the containers, please run `make docker-build`
- After building the containers, run `make docker-start` to start them. At this point the project is already running however, a few more steps needs to be followed before we can access the project on the browser. Please find them below.
- On another terminal tab/window, run `make django-migrate` so the database can be created.
- In order to create a superuser, run `make django-createsuperuser` to create a `Django` superuser to access the admin panel.
- The admin panel can be accessed through `locahost:8000/admin` with the same credentials just created.

At this point, it's possible to go to `localhost:8000` and use the shortening service.

# How to run the tests

The tests can be ran by using one of the following commands (preferably on a new terminal window/tab):

- `make tests`: Runs all the tests
- `make tests-cov`: Runs all the tests with coverage that can be seen inside the folder `htmlcov` located on the root of the project
`make test TEST=path/to/test`: Run an specific test

All of the commands above accept an argument called `ARGS` that can be used to pass arguments like `-v` for verbosity or `-x` to indicate to pytest to stop the test execution if a test fail. The usage is as follows:

- `make django-tests-report ARGS='-vvx'`
