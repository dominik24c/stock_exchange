from django.urls import path

from .views import stock_exchange_list_view, get_stock_exchange_data

app_name = __name__

urlpatterns = [
    path('', stock_exchange_list_view, name='list'),
    path('data/', get_stock_exchange_data, name='data')
]
