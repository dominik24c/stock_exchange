from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render

from .core import get_stock_exchange_from_redis


@login_required
def stock_exchange_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'stock_exchange/list.html', {})


@login_required
def get_stock_exchange_data(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"stock_exchange": get_stock_exchange_from_redis()})
