def verify_status_code(response_data, expect_data):
    assert response_data == expect_data, "Expected HTTP Status code"


def verify_json_key_for_not_null(key):
    assert key != 0, "Key is non Empty" + key
    #assert key > 0, "Key is greater than zero"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Key is non Empty" + key

def verify_response_key(key, expected_data):
    assert key == expected_data


def verify_response_key_should_not_be_none(key):
    assert key is not None
