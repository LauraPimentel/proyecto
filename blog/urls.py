from django.conf.urls import url, include
from blog.views import index

urlpatterns = [
        url(r'^$', index),
    ]
