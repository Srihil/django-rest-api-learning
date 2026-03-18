import requests

endpoint = "http://httpbin.org/status/200"
endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint)
print(get_response.text)
print(get_response.json())