from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from library_manager.models import Product
from rest_framework.validators import UniqueValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = ['id', 'name', 'barcode', 'seller', 'price', 'stock']
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.barcode = validated_data.get('barcode', instance.barcode)
        instance.seller = validated_data.get('seller', instance.seller)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.price = validated_data.get('price', instance.price) 
        instance.save()
        return instance

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class ProductRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)
    barcode = serializers.CharField(write_only=True, required=True)
    seller = serializers.IntegerField(write_only=True, required=True)
    stock = serializers.IntegerField(write_only=True, required=True)
    price = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Product
        fields = ('name','author', 'seller', 'year','stock', 'price')
        extra_kwargs = {
            'stock': {'required': True},
            'price': {'required': True}
        }

    def validate(self, attrs):
        for i in Product.objects.all():
            if attrs['name'] == i.name and attrs['barcode'] == i.barcode and attrs['seller'] == i.seller:
                raise serializers.ValidationError({"Product": "It is already a record with this product at the same seller"})
        return attrs

    def create(self, request, validated_data):
        product = Product.objects.create( 
            name=validated_data['name'],
            barcode=validated_data['barcode'],
            seller= request.user.id,
            stock = validated_data['stock'],
            price = validated_data['price']

        )
        product.save()
        return product

class ProductPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = ['id', 'name', 'barcode', 'seller', 'price', 'stock']
    