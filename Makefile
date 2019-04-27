.PHONY: test

deps:
	pip install -r requirements.txt;\
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test:
	PYTHONPATH=. py.test --verbose -s --html=report.html

run:
	python main.py

docker_build:
	docker build -t flask-hello-world .

docker_run: docker_build
	docker run \
	--name flask-hello-world-dev \
	-p 5000:5000 \
	-d flask-hello-world

USERNAME=adriandolniak
TAG=$(USERNAME)/flask-hello-world

docker_push: docker_build
	@docker login --username $(USERNAME)  --password $${DOCKER_PASSWORD}; \
	docker tag flask-hello-world $(TAG); \
	docker push $(TAG); \
	docker logout;
