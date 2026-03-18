import json
from django.forms.models import model_to_dict
from products.models import Product
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializers

@api_view(["GET"])
def api_home(requests, *args, **kwargs):
  """
  DRF API View
  """
  
  instance = Product.objects.all().order_by("?").first()
  data = {}
  if instance:
    # data = model_to_dict(instance)
    data = ProductSerializers(instance).data
  return Response(data)
  