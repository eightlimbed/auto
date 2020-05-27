clean:
	find . -name '__pycache__' | xargs rm -rf {}
	find . -name '.pytest_cache' | xargs rm -rf {}
	find . -name '*.pyc' | xargs rm -rf {}
	
smoke_tests:
	@echo "Sending GET request WITHOUT Accept header..."
	@curl -XGET --silent localhost:5000
	@echo
	@echo
	@echo "Sending POST request WITHOUT Accept header..."
	@curl -XPOST --silent localhost:5000
	@echo
	@echo
	@echo "Sending GET request WITH Accept header..."
	@curl -XGET -H 'Accept: application/json' localhost:5000
	@echo
	@echo "Sending POST request WITH Accept header..."
	@curl -XPOST -H 'Accept: application/json' localhost:5000
	@echo

test:
	pytest -sv