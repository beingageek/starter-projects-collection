# Run a single Python script without creating a docker image
docker run -it --rm --name python-app -v "$PWD":/usr/src/app -w /usr/src/app python:3-slim python python_hello_world.py
