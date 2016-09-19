from django.conf.urls import url
from .views import recipes_view


urlpatterns = [
    url(r'^$', recipes_view),
]
