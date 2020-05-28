import json
import pytest
import responses
import requests
from requests.exceptions import ConnectionError


API_URI = 'http://127.0.0.1:5000/'


@responses.activate
def test_route_handles_get_and_post_methods():
    """
    Tests that the '/' endpoint handles GET and POST requests.
    The endpoint will also handle HEAD and OPTIONS methods, but all
    other request methods should return 405 (method not allowed)
    """
    responses.add(responses.GET, API_URI)
    responses.add(responses.POST, API_URI)

    r = requests.get(API_URI)
    assert r.status_code == 200

    r = requests.post(API_URI)
    assert r.status_code == 200

    with pytest.raises(ConnectionError):
        r = requests.delete(API_URI)
        assert r.status_code == 405


@responses.activate
def test_get_request_returns_html_if_accept_header_is_not_application_json():
    """
    A GET request should return a string that represents HTML if the header
    does not include 'Accept: application/json'
    """
    responses.add(responses.GET, API_URI, body='<p>Hello, World</p>')

    headers = {}
    r = requests.get(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'

    headers = {'Accept': 'application/xml'}
    r = requests.get(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'


@responses.activate
def test_post_request_returns_html_if_accept_header_is_not_application_json():
    """
    A POST request should return a string that represents HTML if the header
    does not include 'Accept: application/json'
    """
    responses.add(responses.POST, API_URI, body='<p>Hello, World</p>')

    headers = {}
    r = requests.post(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'

    headers = {'Accept': 'application/xml'}
    r = requests.post(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'


@responses.activate
def test_get_request_returns_json_if_accept_header_is_application_json():
    """
    A GET request should return a string that represents JSON if the header
    includes 'Accept: application/json'
    """
    responses.add(responses.GET, API_URI, body='{"message":"Hello, World"}')

    headers = {'Accept': 'application/json'}
    r = requests.get(API_URI, headers=headers)
    assert r.json() == {'message': 'Hello, World'}


@responses.activate
def test_post_request_returns_json_if_accept_header_is_application_json():
    """
    A POST request should return a string that represents JSON if the header
    includes 'Accept: application/json'
    """
    responses.add(responses.POST, API_URI, body='{"message":"Hello, World"}')

    headers = {'Accept': 'application/json'}
    r = requests.post(API_URI, headers=headers)
    assert r.json() == {'message': 'Hello, World'}
