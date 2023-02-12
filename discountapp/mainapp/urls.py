from django.urls import path
from mainapp.views import error_handler

urlpatterns = [
     path('errors/<int:status/_code>', error_handler)
]
