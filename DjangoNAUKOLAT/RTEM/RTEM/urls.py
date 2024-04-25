"""
URL configuration for RTEM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='Home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='Home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Home.views import home_view, about_view
from MZE.views import chart_view
from PZ.views import predict
from SG.views import EnergyPricesView, show_chart

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home_view"),
    path("MZE/", chart_view, name="chart_view"),
    path("about/", about_view, name="about_view"),
    path("PZ/", predict, name="forecast_energy"),
    # path("SG/", energy_data_view, name="energy_data_view"),
    path('fetch_data/', EnergyPricesView.as_view(), name='fetch_data'),
    path('SG/', show_chart, name='show_chart'),
]
