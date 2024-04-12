# Create Token
# Create Toke
# Update the Booking(PUT)
# Delete the Booking

# verify that created booking id when we update we are able to update it and delete it.
# create tokem
# Create booking
# test_update()
# fixtures -> pass the data in pytest

import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCRUDBooking(object):

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(self),
                                headers=Util.common_headers_json(self),
                                auth=None,
                                payload=payload_create_token(),
                                in_json=False)
        verify_status_code(response_data=response.status_code, expect_data=200)
        # verify_json_key_for_not_null_token(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture()
    def get_booking_id(self):
        response = post_request(url=APIConstants.url_create_booking(self),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        booking_id = response.json()["bookingid"]
        actual_status_code = response.status_code
        verify_status_code(response_data=actual_status_code, expect_data=200)
        verify_json_key_for_not_null_token(booking_id)
        return booking_id

    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description("Verify that full update with booking id and token.")
    def test_update_booking_id_put(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_request(url=put_url,
                               headers=Util.common_header_put_delete(token=token),
                               payload=payload_Update_booking_PUT(),
                               auth=None,
                               in_json=False
                               )
        verify_status_code(response_data=response.status_code, expect_data=200)
        verify_json_key_for_not_null(response.json()["firstname"])

    @allure.title("Test CRUD operation Update(Patch).")
    @allure.description("Verify that partial update with booking id and token.")
    def test_update_booking_id_patch(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = patch_request(url=patch_url,
                                 headers=Util.common_header_put_delete(token=token),
                                 payload=payload_update_booking_patch(),
                                 auth=None,
                                 in_json=False
                                 )
        verify_status_code(response_data=response.status_code, expect_data=200)
        verify_json_key_for_not_null(response.json()["firstname"])
        verify_response_key(response.json()["firstname"], expected_data="Shivam")
        verify_response_key(response.json()["lastname"], expected_data="Shelke")

    @allure.title("Test CRUD operation delete")
    @allure.description("Verify booking gets deleted with the booking ID and token.")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_request(url=delete_url,
                                  headers=Util.common_header_put_delete(token=token),
                                  auth=None,
                                  in_json=False
                                  )
        verify_status_code(response_data=response.status_code, expect_data=201)
