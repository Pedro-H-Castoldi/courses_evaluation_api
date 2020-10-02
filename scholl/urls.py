from django.contrib import admin
from django.urls import path, include

from courses.urls import router

urlpatterns = [
    path('api/v1/', include('courses.urls')),
    # Inserindo todas as rotas geradas na url de courses com o objeto router (note q  agora é a v2 da api)
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
