from django.urls import path

from mainapp.views import error_handler, index

urlpatterns = [
     path('errors/<int:status_code>', error_handler),
     path('', index),
]
