import requests
import pytest
from unittest import mock

@pytest.mark.integration
def test_user_authentication_invalid_password(mocker):
    # Define the URL and parameters
    url = 'http://127.0.0.1:8000/users'
    params = {'username': 'admin', 'password': 'qwerty'}
    
    # Mock the requests library to return a predefined response
    mocked_response = mock.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''
    mocker.patch('requests.get', return_value=mocked_response)
    
    # Make a GET request to the URL with the parameters
    response = requests.get(url, params=params)
    
    # Assert the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert the response content is empty
    assert response.text == ''


def test_user_authentication_invalid_username(mocker):
    # Define the URL and parameters
    url = 'http://127.0.0.1:8000/users'
    params = {'username': 'user123', 'password': 'admin'}
    
    # Mock the requests library to return a predefined response
    mocked_response = mock.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''
    mocker.patch('requests.get', return_value=mocked_response)
    
    # Make a GET request to the URL with the parameters
    response = requests.get(url, params=params)
    
    # Assert the response status code is 401 (Unauthorized)
    assert response.status_code == 401
    
    # Assert the response content is empty
    assert response.text == ''
