import pytest
import allure

from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.utils.utils import Util


class TestUpdateBookingPatch(object):

    @pytest.mark.positive
    @allure.title("Verify Update booking with patch API")
    @allure.description("Verify update booking patch")
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

    @pytest.mark.Negative
    @allure.title("Verify Update booking with empty payload")
    @allure.description("Update partial booking should get failed with empty payload")
    def test_update_booking_id_empty_payload(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = patch_request(url=patch_url,
                                 auth=None,
                                 headers=Util.common_header_put_delete(token=token),
                                 payload=payload_update_booking_patch_negative(),
                                 in_json=False)
        verify_status_code(response_data=response.status_code, expect_data=400)
