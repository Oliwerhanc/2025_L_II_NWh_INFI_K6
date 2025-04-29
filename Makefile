# Makefile

# Zmienna dla tagu obrazu Docker
DOCKER_IMAGE_NAME=hello-world-printer

# Zadanie do budowania obrazu Docker
docker_build:
	docker build -t $(DOCKER_IMAGE_NAME) .
