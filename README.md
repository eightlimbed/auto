# auto_api
auto_api is a simple "Hello, World" HTTP server that returns HTML and JSON.

## Requirements
**This program requires [Docker](https://docs.docker.com/get-docker/)**.

 `make` is used for convenience. If you don't have `make`, cannot install it, or prefer to see use the underlying commands, please see **Running without make** at the bottom of this page.

## Quickstart
```bash
# Run the API in a container (must have port 5000 available)
$ make run

# Test the endpoint
$ curl localhost:5000
$ curl -H 'Accept: application/json' localhost:5000

# Stop the server and remove the container
$ make stop
```

## Run Unit Tests

To run the unit tests, use the following command:
```bash
$ make test
```
You do not need to have the server running to execute the unit tests because the responses have been mocked.

## Debug Mode
In debug mode, log statements will be printed for each request that includes a timestamp and the request URL. To run the server in debug mode use the following command:
```bash
$ make debug
```
The server process will be at the forefront of your terminal so you can see the logs.

You can then `curl` the endpoint from another terminal and see the log output printed in the terminal that the server is running in.
```bash
$ curl localhost:5000
$ curl -H 'Accept: application/json' localhost:5000
```

## Foreground Mode
If you would like to run the server in the foreground of your terminal, use the following command:
```bash
$ make run_foreground
```

## Running without Make
```bash
# Build the docker image
$ docker build -t auto_api .

# Run the server (in the background) on port 5000
$ docker run -d -p 5000:5000 auto_api

# Run the server in debug mode
$ docker run -p 5000:5000 -e DEBUG=True auto_api

# Test the endpoint
$ curl localhost:5000
$ curl -H 'Accept: application/json' localhost:5000
```

## Cleanup
To remove any lingering `auto_api` containers, use the following command:
```bash
$ make stop
```

## Troubleshooting
You may run into one of the following errors

> Bind for 0.0.0.0:5000 failed: port is already allocated

This means there is another process using port 5000. If you already ran an `auto_api` container you can kill it by running `make stop`, and then try again. Otherwise, you will need to stop the other service on your machine that is using port 5000, or you can run the `auto_api` server on port 8888, for example, using the following command: 
```bash
$ docker run -d -p 8888:5000 auto_api
```

> Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

This means that Docker is not running on your machine. Please start up Docker and try again.