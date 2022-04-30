from django.urls import path
from .views import ProductListCreateView

app_name = 'product'

urlpatterns = [
    path('', ProductListCreateView.as_view(),)
]
