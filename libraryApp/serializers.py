from rest_framework import serializers
from .models import Students,Books,Library

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Library
        fields='__all__'