import allure
import pytest

from conftest import create_token
from src.constants.api_constants import APIConstants
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *
from src.helpers.api_requests_wrapper import *
import logging


class TestCRUDBooking(object) :
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_id (self) :
        payload = payload_create_booking()
        response = post_request(
            url=APIConstants().url_create_booking(),
            headers=Utils().common_headers_json(),
            auth=None,
            payload=payload,
            in_json=False
        )
        resp = response.json()
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(resp["bookingid"])
        verify_response_key(resp["booking"]["firstname"], payload["firstname"])
        # logger.info("Verify the Firstname tag value between Request and Response-",resp["booking"]["firstname"] ," and",  payload["firstname"])
        print("Verify the Firstname tag value between Request and Response-", resp["booking"]["firstname"], " and",
              payload["firstname"])


@pytest.mark.put
@allure.title("Test CRUD operation Update(PUT).")
@allure.description(
    "Verify that Full Update with the booking ID and Token is working.")
def test_update_booking_id_token (self, create_token, get_booking_id) :
    put_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
    print(put_url)
    response = put_requests(
        url=put_url,
        headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
        payload=payload_update_booking(),
        auth=None,
        in_json=False
    )
    # Verification here & more
    verify_response_key(response.json()["firstname"], "Amit")
    verify_response_key(response.json()["lastname"], "Brown")
    verify_http_status_code(response_data=response, expected_data=200)


def test_delete_booking_id (self, create_token, get_booking_id) :
    delete_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
    response = delete_requests(
        url=delete_url,
        headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
        auth=None,
        in_json=False
    )
    verify_response_delete(response=response.text)
    verify_http_status_code(response_data=response, expected_data=201)
