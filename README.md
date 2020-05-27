# auto_api
auto_api is a simple "Hello, World" HTTP server that returns HTML or JSON depending on the `Accept` header value.

# Requirements
**This program requires [Docker](https://docs.docker.com/get-docker/) and [Make](https://www.gnu.org/software/make/)**. Make is only used for convenience. If you don't have Make, or cannot install it, please see _Running without Make_ at the bottom of this page.

# Quickstart
```bash
# Build the Docker image
$ make build

# Run the API in a container (must have port 5000 available)
$ make run

# Test the endpoint
$ make smoke_tests
```

### Run Tests

```
make run_tests
```

### Running without Make

```
```