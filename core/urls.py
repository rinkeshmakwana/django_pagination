from django.urls import path
from django.conf.urls import url
from .views import ClientSideView, ServerSideView, LazyLoadView

urlpatterns = [
    path('client-side/', ClientSideView.as_view(), name='client-side'),
    path('server-side/', ServerSideView.as_view(), name='server-side'),
    path('lazy-load/', LazyLoadView.as_view(), name='lazy-load'),
]