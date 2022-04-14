@echo off

rem Create docker image
docker build -t python-starter .

rem Run docker image
docker run -it --rm --name python-app python-starter