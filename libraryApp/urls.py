from django.urls import path
from .views import *

urlpatterns=[
path('get_students/',list_all_students,name='getAllStudents'),
path('post_student/',add_student,name='postStudent'),
path('update_student/<str:id>',update_student,name='update_student'),
path('delete_student/<str:id>',delete_student,name='delete_student'),

path('get_books/',list_all_books,name='getAllbooks'),
path('post_book/',add_book,name='postbook'),
path('update_book/<str:id>',update_book,name='update_book'),
path('delete_book/<str:id>',delete_book,name='delete_book'),

path('get_library/',list_all_library,name='getAlllibrary'),
path('post_library/',add_library,name='postlibrary'),
path('update_library/<int:id>',update_library,name='update_library'),
path('renewal_book/<int:id>',renewal_book,name='update_library'),
path('return_book/<int:id>',return_book,name='return_book')
] 