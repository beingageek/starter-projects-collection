# Create docker image
docker build -t python-starter .

# Run docker image
docker run -it --rm --name python-app python-starter