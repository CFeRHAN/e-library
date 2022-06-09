
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from management import views
from .feed import LatestEntriesFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('books/', views.BookListView, name='books'),
    path('books/<int:pk>', views.BookDetailView, name='book-detail'),
    path('books/create/', views.BookCreate, name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdate, name='book_update'),
    path('books/<int:pk>/delete/', views.BookDelete, name='book_delete'),

    path('students/<int:pk>/delete/', views.StudentDelete, name='student_delete'),
    path('students/create/', views.StudentCreate, name='student_create'),
    path('students<int:pk>/update/', views.StudentUpdate, name='student_update'),
    path('students/<int:pk>', views.StudentDetail, name='student_detail'),
    path('students/', views.StudentList, name='student_list'),
    path('students/book_list', views.student_BookListView, name='book_student'),
    path('books/<int:pk>/request_issue/', views.student_request_issue, name='request_issue'),

    path('feed/', LatestEntriesFeed(), name='feed'),
    path('return/<int:pk>', views.ret, name='ret'),
    path('rating/<int:pk>/update/', views.RatingUpdate, name='rating_update'),
    path('rating/<int:pk>/delete/', views.RatingDelete, name='rating_delete'),
    path('api/', include('api.urls')),

    re_path(r'^search_b/', views.search_book, name="search_b"),
    re_path(r'^search_s/', views.search_student, name="search_s"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
