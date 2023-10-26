import requests,pytest


def test_api():
    url = "http://localhost:5000/"
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 200


# from rest_framework.test import APIClient
# import pytest
# client = APIClient()
# @pytest.getgist
# def test_getgist(/):
#     response = client.get('/')
#     assert response.status_code == 200

