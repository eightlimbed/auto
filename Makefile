clean:
	find . -name '__pycache__' | xargs rm -rf {}
	find . -name '.pytest_cache' | xargs rm -rf {}
	find . -name '*.pyc' | xargs rm -rf {}

build:
	docker build -t auto_api .

run: build
	docker run --rm -d -p 5000:5000 auto_api	

run_foreground:
	docker run --rm -p 5000:5000 auto_api	

stop:
	docker ps -q --filter "label=app=auto_api" | xargs docker rm -f

test: build
	docker run --rm -it auto_api pytest -sv

debug: build
	docker run --rm -p 5000:5000 -e DEBUG=True auto_api	