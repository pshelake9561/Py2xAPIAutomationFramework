import pytest
import allure

from src.constants.api_constants import *
from src.utils.utils import Util
from src.helpers.payload_manager import payload_create_token
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *


class TestCreateToken(object):

    @pytest.mark.positive
    @allure.title("Test Create Token API")
    @allure.description("Verify Create token functionality")
    def test_create_token(self):
        response = post_request(url=APIConstants.url_create_token(self),
                                headers=Util.common_headers_json(self),
                                payload=payload_create_token(),
                                auth=None,
                                in_json=False
                                )
        verify_status_code(response_data=response.status_code, expect_data=200)
        verify_json_key_for_not_null_token(response.json()["token"])
