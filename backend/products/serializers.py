from rest_framework import serializers
from rest_framework.reverse import reverse 
from .models import Product
from .validators import validate_title

class ProductSerializers(serializers.ModelSerializer):
  my_discount = serializers.SerializerMethodField(read_only=True)
  edit_url = serializers.SerializerMethodField(read_only=True)
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field = 'pk')

  title = serializers.CharField(validators=[validate_title])
  class Meta:
    model = Product
    fields = [
      'url',
      'edit_url',
      'pk',
      'title',
      'content',
      'price',
      'sales_price',
      'my_discount',
    ]

  # def create(self, validated_data):
  #   return super().create(validated_data)

  # def update(self,instance, validated_data):
  #   instance.title = validated_data.get('title')
  #   return instance
  
  def get_edit_url(self, obj):
    request = self.context.get('request')
    if request is None:
      return None
    return reverse("product-edit", kwargs={"pk" : obj.pk}, request=request)

  def get_my_discount(self, obj):
    if not hasattr(obj, 'id'):
      return None
    if not isinstance(obj, Product):
      return None
    return obj.get_discount()
    