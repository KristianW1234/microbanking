"""
URL configuration for microbanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from api.controllers.customer_controller import add_customer, get_customer_by_id, update_customer, delete_customer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/customer/add/", add_customer),
    path("api/v1/customer/get/<int:customer_id>", get_customer_by_id),
    path("api/v1/customer/update/", update_customer),
    path("api/v1/customer/delete/<int:customer_id>", delete_customer),
]
