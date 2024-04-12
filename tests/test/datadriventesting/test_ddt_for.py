import openpyxl
import requests

from src.constants.api_constants import APIConstants
from src.utils.utils import Util
def read_credentials_from_excel():
    credentials = []
    workbook = openpyxl.load_workbook(filename=)


def create_auth_request(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=APIConstants.url_create_token(),
                             headers=Util.common_headers_json(),
                             auth=None,
                             payload=payload),
                             In_json = False
    return response


def test_create_auth_with_excel():
    pass
