from django.conf.urls import url
from .views import view_basket, add_to_basket, edit_basket

urlpatterns = [
    url(r'^$', view_basket, name='view_basket'),
    url(r'^add/(?P<id>\d+)', add_to_basket, name='add_to_basket'),
    url(r'^edit/(?P<id>\d+)', edit_basket, name='edit_basket'),
]
