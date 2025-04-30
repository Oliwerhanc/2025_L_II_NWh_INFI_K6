DOCKER_IMAGE_NAME=hello-world-printer

docker_build:
	DOCKER_BUILDKIT=1 docker build --platform=linux/amd64 -t $(DOCKER_IMAGE_NAME) .