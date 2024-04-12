import pytest
import allure


from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create booking Status and booking Id shouldn't null")
    @allure.description(
        "Create a Booking from the payload and verify that booking id should not be null and status code should be "
        "200 for the correct payload")
    def test_create_booking_positive(self):
        response = post_request(url=APIConstants.url_create_booking(self),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        booking_id = response.json()["bookingid"]
        actual_status_code = response.status_code
        verify_status_code(response_data=actual_status_code,expect_data=200)
        verify_json_key_for_not_null(booking_id)

    @pytest.mark.negative
    @allure.title("Verify that Create booking Status code with empty payload")
    @allure.description(
        "Create a Booking from the empty payload and verify that the status code should be 500 for the empty payload")
    def test_create_booking_tc2(self):
        response = post_request(url=APIConstants.url_create_booking(self),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload={},
                                in_json=False)
        actual_status_code = response.status_code
        verify_status_code(response_data=actual_status_code,expect_data=500)

    @pytest.mark.positive
    @allure.title("Verify the getBookingIds API functionality")
    @allure.description("The getBookingIds API should Get the list of all booking IDs")
    def test_get_booking_ids(self):
        response = get_request(url=APIConstants.url_create_booking(self),
                               auth=None
                               )
        actual_status_code = response.status_code
        verify_status_code(response_data=actual_status_code, expect_data=200)
