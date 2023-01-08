from rest_framework import routers
from .views import TodoViewSet

routers = routers.DefaultRouter()
routers.register('api/todos',TodoViewSet,'todos')

urlpatterns = routers.urls
