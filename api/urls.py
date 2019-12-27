from django.urls import path,re_path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('values', views.StoreDataView.as_view(), name="key_value"),
]
