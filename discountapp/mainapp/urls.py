from django.urls import path
from mainapp.views import error_handler

urlpatterns = [
     path('errors/<int:status_code>', error_handler)
]
