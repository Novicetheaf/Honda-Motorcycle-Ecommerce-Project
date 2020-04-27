from django.conf.urls import url, include
from .views import all_motorcycles

urlpatterns = [
    url(r'^$', all_motorcycles, name='motorcycles'),
]
