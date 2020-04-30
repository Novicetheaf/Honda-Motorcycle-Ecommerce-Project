from django.conf.urls import url, include
from .views import get_shop_reviews, shop_review_detail, add_or_edit_shop_review


urlpatterns = [
    url(r'^$', get_shop_reviews, name='get_shop_reviews'),
    url(r'^(?P<pk>\d+)/$', shop_review_detail, name='shop_review_detail'),
    url(r'^new/$', add_or_edit_shop_review, name='add_shop_review'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_shop_review, name='edit_shop_review')
]
