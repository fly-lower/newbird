from . views import *
from django.urls import path,re_path


urlpatterns = [
    path('index/',index),
    path('addperson/',addperson),
    path('selectperson/',selectperson),
    path('getbook_publish/',getbook_publish),
    path('Addbook_publish/',Addbook_publish),
    path('Addpublish/',Addpublish),
    path('Delpublish/',Delpublish),
    path('Addbook_publish/',Addbook_publish),
    path('updatebook_publish/',updatebook_publish),
    path('addtoto/',addtoto),
    path('updatetoto/',updatetoto),
    path('deltoto/',deltoto),
    path('aggregate_get/',aggregate_get),
]