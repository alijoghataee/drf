from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=150)
    story_name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    image = serializers.ImageField(default='', use_url=True)
    fav = serializers.BooleanField(default=False)


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
