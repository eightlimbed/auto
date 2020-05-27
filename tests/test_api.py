import json
import pytest
import requests


API_URI = 'http://127.0.0.1:5000/'


def test_route_handles_get_and_post_methods():
    """
    Tests that the '/' endpoint handles GET and POST requests.
    The endpoint will also handle HEAD and OPTIONS methods, but all
    other request methods should return 405 (method not allowed)
    """
    r = requests.get(API_URI)
    assert r.status_code == 200

    r = requests.post(API_URI)
    assert r.status_code == 200

    r = requests.delete(API_URI)
    assert r.status_code == 405


def test_get_request_returns_html_if_accept_header_is_not_application_json():
    """
    A GET request should return a string that represents HTML if the header
    does not include 'Accept: application/json'
    """
    headers = {}
    r = requests.get(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'

    headers = {'Accept': 'application/xml'}
    r = requests.get(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'


def test_post_request_returns_html_if_accept_header_is_not_application_json():
    """
    A POST request should return a string that represents HTML if the header
    does not include 'Accept: application/json'
    """
    headers = {}
    r = requests.post(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'

    headers = {'Accept': 'application/xml'}
    r = requests.post(API_URI, headers=headers)
    assert r.text == '<p>Hello, World</p>'


def test_get_request_returns_json_if_accept_header_is_application_json():
    """
    A GET request should return a string that represents JSON if the header
    includes 'Accept: application/json'
    """
    headers = {'Accept': 'application/json'}
    r = requests.get(API_URI, headers=headers)
    assert r.json() == {'message': 'Hello, World'}


def test_post_request_returns_json_if_accept_header_is_application_json():
    """
    A POST request should return a string that represents JSON if the header
    includes 'Accept: application/json'
    """
    headers = {'Accept': 'application/json'}
    r = requests.post(API_URI, headers=headers)
    assert r.json() == {'message': 'Hello, World'}
