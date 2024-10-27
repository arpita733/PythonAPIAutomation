# payloads

def payload_create_booking():
    payload = {
    "firstname" : "Arpita",
    "lastname" : "Mukherjee",
    "totalprice" : 1500.00,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-09-28",
        "checkout" : "2024-10-15"
    },
    "additionalneeds" : "Breakfast"
}
    return payload


def payload_update_booking():
    payload = {
    "firstname": "Aishani",
    "lastname": "Mukherjee",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-09-28",
        "checkout": "2024-10-15"
    },
    "additionalneeds": "Breakfast"
}
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload