import requests

endpoint = "http://localhost:8000/api/products/8769897422424123141414247/"

get_response = requests.get(endpoint)
print(get_response.json()) 