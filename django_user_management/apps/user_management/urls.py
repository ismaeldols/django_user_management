from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


endpoint_urlpatterns = [
        path('', include(router.urls)),
]

api_urlpatterns = [
    path('rest/', include(endpoint_urlpatterns)),
]

urlpatterns = [
    path('<str:version>/', include(api_urlpatterns))
]
