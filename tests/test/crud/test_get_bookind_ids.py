import pytest
import allure

from src.utils.utils import Util
from src.helpers.api_requests_wrapper import get_request
from src.helpers.common_verification import *
from src.constants.api_constants import APIConstants


class TestGetBookingIds(object):

    @pytest.mark.positive
    @allure.title("Verify GetBookingIds API functionality ")
    @allure.description("Verify the get Booking Ids API")
    def test_get_booking_ids(self):
        response = get_request(url=APIConstants.url_create_booking(self),
                               auth=None
                               )
        verify_status_code(response_data=response.status_code, expect_data=200)
