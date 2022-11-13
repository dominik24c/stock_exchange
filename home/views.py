from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/main.html', {})
