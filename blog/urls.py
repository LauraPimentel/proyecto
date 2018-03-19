from django.conf.urls import url, include
from blog.views import index, alumno_view

urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^nuevo$', alumno_view, name='alumno_crear'),
    ]
