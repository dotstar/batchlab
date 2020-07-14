build:
	docker build  -t  matrixmath --no-cache --compress .

run:
	docker run --rm -it matrixmath

tag:
	docker tag matrixmath:latest dotstar/matrixmath:v1

push: tag
	docker push dotstar/matrixmath:v1
