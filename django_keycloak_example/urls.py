"""
URL configuration for django_keycloak_example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import include, path
from keycloak import views as keycloak_views


# Admin Site Config
admin.sites.AdminSite.site_header = "Django Keycloak Example"
admin.sites.AdminSite.site_title = "Admin"
admin.sites.AdminSite.index_title = "Django Keycloak Example"


@csrf_exempt
def echo(request: HttpRequest):
    """
    Print query params and return the same into response
    """
    print(request.GET)
    return HttpResponse(request.GET.items())


urlpatterns = [
    path("", include("oauth2_authcodeflow.urls")),
    path("echo/", echo, name="echo"),
    path(
        f"admin/login/",
        keycloak_views.DjangoAdminLoginView.as_view(),
        name="admin_login",
    ),
    path(
        f"admin/logout/",
        keycloak_views.DjangoAdminLogoutView.as_view(),
        name="admin_logout",
    ),
    path("admin/", admin.site.urls),
]
