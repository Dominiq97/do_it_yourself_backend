from rest_framework import serializers

from library_manager.models import Publisher, Book
from rest_framework.validators import UniqueValidator


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Book
        fields = ['id', 'title', 'publisher', 'author','year', 'price','stock']
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.year = validated_data.get('year', instance.year)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def create(self, validated_data):
        return Book.objects.create(**validated_data)



class PublisherSerializer(serializers.ModelSerializer):
    book = BookSerializer(source='book_set', many=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'book']

class BookRegisterSerializer(serializers.ModelSerializer):
    title = serializers.CharField(write_only=True, required=True)
    author = serializers.CharField(write_only=True, required=True)
    publisher = serializers.IntegerField(write_only=True, required=True)
    year = serializers.CharField()
    stock = serializers.IntegerField(write_only=True, required=True)
    price = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Book
        fields = ('title','author', 'publisher', 'year','stock', 'price')
        extra_kwargs = {
            'stock': {'required': True},
            'price': {'required': True}
        }

    def validate(self, attrs):
        for i in Book.objects.all():
            if attrs['title'] == i.title and attrs['author'] == i.author and attrs['publisher'] == i.publisher:
                raise serializers.ValidationError({"Book": "It is already a record with this title at the same publisher"})
        return attrs

    def create(self, validated_data):
        book = Book.objects.create( 
            title=validated_data['title'],
            author=validated_data['author'],
            publisher=validated_data['publisher'],
            year = validated_data['year'],
            stock = validated_data['stock'],
            price = validated_data['price']

        )
        book.save()
        return book

    
