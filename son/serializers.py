from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author_serializer = AuthorSerializer(data=author_data)
        if author_serializer.is_valid():
            author = author_serializer.save()
            book = Book.objects.create(author=author, **validated_data)
            return book
        else:
            raise serializers.ValidationError(author_serializer.errors)
