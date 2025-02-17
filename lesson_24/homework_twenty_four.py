"""This module tests 'Flask-app.py module.'"""

import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth


logging.basicConfig(
    filename='test_search.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


@pytest.fixture(scope='class')
def authenticated_session():
    url = 'http://127.0.0.1:8080/auth'
    session = requests.Session()
    response = session.post(url, auth=HTTPBasicAuth('test_user', 'test_pass'))

    assert response.status_code == 200, 'Authentication failed.'
    token = response.json().get('access_token')
    assert token, 'Token not received'


    session.headers.update({'Authorization': f'Bearer {token}'})
    return session


@pytest.mark.parametrize(
    'sort_by, limit',
    [
        (None, None),
        ('price', 5),
        ('year', 10),
        ('engine_volume', 3),
        ('brand', 7),
        ('price', 1),
        ('year', 20),
    ],
)
def test_search_cars(authenticated_session, sort_by, limit):
    base_url = 'http://127.0.0.1:8080/cars'
    params = {}

    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    response = authenticated_session.get(base_url, params=params)

    logging.info(f'GET {base_url} with params {params} - Status Code: {response.status_code}')
    logging.info(f'Response: {response.json()}')

    assert response.status_code == 200, f'Error: {response.status_code}'
    cars = response.json()

    if limit:
        assert len(cars) <= int(limit), f'Amount exceeds limit {limit}!'
    if sort_by:
        assert all(cars[i][sort_by] <= cars[i + 1][sort_by] for i in range(len(cars) - 1)), \
            f'Results are not sorted by {sort_by}!'
