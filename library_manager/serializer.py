from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from library_manager.models import Publisher, Product
from rest_framework.validators import UniqueValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = ['id', 'title', 'seller', 'author','year', 'price','stock']
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.seller = validated_data.get('seller', instance.seller)
        instance.year = validated_data.get('year', instance.year)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.price = validated_data.get('price', instance.price) 
        instance.save()
        return instance

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class ProductRegisterSerializer(serializers.ModelSerializer):
    title = serializers.CharField(write_only=True, required=True)
    author = serializers.CharField(write_only=True, required=True)
    seller = serializers.IntegerField(write_only=True, required=True)
    year = serializers.CharField()
    stock = serializers.IntegerField(write_only=True, required=True)
    price = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Product
        fields = ('title','author', 'seller', 'year','stock', 'price')
        extra_kwargs = {
            'stock': {'required': True},
            'price': {'required': True}
        }

    def validate(self, attrs):
        for i in Product.objects.all():
            if attrs['title'] == i.title and attrs['author'] == i.author and attrs['seller'] == i.seller:
                raise serializers.ValidationError({"Product": "It is already a record with this title at the same seller"})
        return attrs

    def create(self, validated_data):
        product = Product.objects.create( 
            title=validated_data['title'],
            author=validated_data['author'],
            seller=validated_data['seller'],
            year = validated_data['year'],
            stock = validated_data['stock'],
            price = validated_data['price']

        )
        product.save()
        return product

    
