
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
import debug_toolbar
from bookstore import views

urlpatterns = [
    # Debug toolbar
    path("__debug__/", include(debug_toolbar.urls)),

    # Admin
    path("admin/", admin.site.urls),

    # Autenticação por token
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

    # Atualização do servidor
    path("update_server/", views.update, name="update"),

    # Rotas da API por versão
    path("bookstore/<version>/order/", include("order.urls")),
    path("bookstore/<version>/product/", include("product.urls")),
]