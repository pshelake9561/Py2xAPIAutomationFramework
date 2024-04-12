import pytest
import allure

from src.utils.utils import Util
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.constants.api_constants import APIConstants

class TestUpdateFirstName(object):

    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(self),
                                auth=None,
                                headers=Util.common_headers_json(),
                                payload=payload_create_token(),
                                in_json=False)
        token = response.json()["token"]
        return token

    def create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(self),
                                auth=None,
                                headers=Util.common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False
                                )
        booking_id = response.json()["bookingid"]
        return booking_id


    @pytest.mark.integration_test1
    @allure.title("Verify is user able to update first name after creating a booking.")
    @allure.description("After creating a booking user should be able to update the first name")
    def test_update_first_name(self,create_token, booking_id):


