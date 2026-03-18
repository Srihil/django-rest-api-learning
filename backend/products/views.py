from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializers

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers

  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(content=content)

Product_List_Create_View = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers

Product_Detail_View = ProductDetailAPIView.as_view()



class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title

Product_Update_View = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    super().perform_destroy(instance)

Product_delete_View = ProductDestroyAPIView.as_view()





@api_view(['GET', 'POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
  method = request.method

  if method == "GET":
    if pk is not None:
      obj = get_object_or_404(Product, pk=pk)
      data = ProductSerializers(obj, many=False).data
      return Response(data)
    queryset = Product.objects.all()
    data = ProductSerializers(queryset, many=True).data
    return Response(data)
  
  if method == "POST":
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
        content = title
      serializer.save(content=content)
      return Response(serializer.data)
    return Response({"invalid" : "not a valid data"}, status=400)