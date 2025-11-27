from django.urls import path
from . import views

urlpatterns = [
    path("", views.chart_view, name="chart_view"),
]
