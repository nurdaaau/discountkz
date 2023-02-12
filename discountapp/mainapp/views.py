from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def error_handler(request: HttpRequest, status_code: int) -> HttpResponse:
    context = {
        'status_code_error': status_code
    }
    return render(request, "errors.html", context)