
from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/',include('articles.api.urls')),
    path("", index, name="index")
#    path('test/',include('articles.api.urls'))
]
