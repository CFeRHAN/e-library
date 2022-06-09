from rest_framework import serializers
from management.models import Book, Student, Borrower

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('pic', )


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['id', 'account_name', 'users', 'created']
        exclude = ('pic', )


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

