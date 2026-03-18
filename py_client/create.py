import requests



endpoint = "http://localhost:8000/api/products/"

headers = {
  'Authorization': 'Bearer 8ef00c382d5671a0f18b4687d0a75905eb0144d0'
}
data = {
  "title" : "this is done",
}
get_response = requests.post(endpoint, json=data,headers=headers)
print(get_response.json())