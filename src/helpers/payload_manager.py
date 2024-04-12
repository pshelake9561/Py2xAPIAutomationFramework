# payload
from faker import Faker
import json

faker = Faker()


def payload_create_booking():
    payload = {
        "firstname": "Pramod",
        "lastname": "Shelke",
        "totalprice": 501,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-14",
            "checkout": "2024-04-16"
        },
        "additionalneeds": ""
    }
    return payload


def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, maz=1000),
        "depositpaid": faker.boolean,
        "bookingdates": {
            "checkin": "2024-04-14",
            "checkout": "2024-04-16"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "Wife"))
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def payload_Update_booking_PUT():
    payload = {
        "firstname": "prem",
        "lastname": "shelke",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-09",
            "checkout": "2024-04-22"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking_patch():
    payload = {
        "firstname": "Shivam",
        "lastname": "Shelke"
    }
    return payload

def payload_update_booking_patch_negative():
    payload = {}
    return payload