import json
from django.http import JsonResponse

def api_home(requests, *args, **kwargs):
  body = requests.body
  data = {}
  try:
    data = json.loads(body)
  except:
    pass
  print(data)
  data['params'] = dict(requests.GET)
  data['headers'] = dict(requests.headers)
  data['content_type'] = requests.content_type
  return JsonResponse(data)