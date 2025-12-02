import data
import configuration
import requests

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)

response_past = create_order(data.order_body)
print(response_past.status_code)
print(response_past.json())
namber = response_past.json()
print(namber["track"])
track = namber["track"]

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER_PATH, params={"t": track})
response_get = get_order(track)
print(response_get.status_code)
print(response_get.json())

