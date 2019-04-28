.PHONY: test

deps:
	pip install -r requirements.txt;\
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test_smoke:
	curl --fail 127.0.0.1:5000

test:
	PYTHONPATH=. py.test --verbose -s --html=test_report.html

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=.

test_xunit:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml --junit-xml=test_results.xml

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
