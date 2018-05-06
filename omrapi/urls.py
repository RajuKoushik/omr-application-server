from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^omrendpoint/', views.omr_api, name='omrapi'),

]