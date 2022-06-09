from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="erhan@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books_api'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail_api'),

    path('students/', views.StudentList.as_view(), name='students_api'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student_detail_api'),

    path('borrowers/', views.BorrowerList.as_view(), name='borrowers_api'),
    path('borrowers/<int:pk>', views.BorrowerDetail.as_view(), name='borrower_detail_api'),

    # Swagger and Redoc URLS

    # path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
