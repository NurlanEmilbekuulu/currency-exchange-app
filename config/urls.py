from django.conf.urls import handler404
from django.contrib import admin
from django.urls import include, path

handler404 = 'exchange_rates.views.custom_not_found_view'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('exchange_rates.urls')),
]
