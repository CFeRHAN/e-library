from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, generics, mixins, permissions

from management.models import Book, Student, Borrower
from .serializers import BookSerializer, BorrowerSerializer, StudentSerializer


class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BorrowerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

    def get(self, request, *args, **kwargs):
        print(self.serializer_class)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = BorrowerSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.validated_data['book']
            book.available_copies = book.available_copies - 1
            book.save()
            print(f'this is validated data::: ', book)
            print(f'this is -1 stock::: ', book.available_copies)
            # serializer.save()
            return self.create(request, *args, **kwargs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class BorrowerDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        borrower = self.get_object()
        book = borrower.book
        book.available_copies = book.available_copies + 1
        book.save()
        print(f'this is +1 stock::: ', book.available_copies)

        return self.destroy(request, *args, **kwargs)
