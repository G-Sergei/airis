from django.shortcuts import render
from django.http import HttpResponse
import global_custom_setting as gcs


def index(request):
    return render(request, 'index.html', {
        'order_limit': 'Принимаем заказы на сумму от 15 000 р.',
        # Выводить банер или нет - указано в настройках сайта
        'order_limit_view': gcs.ORDER_LIMIT_VIEW,
        'title': gcs.TITLE,
    })

# Create your views here.
