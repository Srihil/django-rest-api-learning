import json
from django.forms.models import model_to_dict
from products.models import Product
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializers

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
  