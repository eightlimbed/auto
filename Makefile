clean:
	find . -name '__pycache__' | xargs rm -rf {}
	find . -name '.pytest_cache' | xargs rm -rf {}
	find . -name '*.pyc' | xargs rm -rf {}
	
test:
	pytest -sv