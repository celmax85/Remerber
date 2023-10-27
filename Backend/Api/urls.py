from rest_framework import routers
from .api import UserViewSet, FichierViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/fichiers', FichierViewSet, 'fichiers')

urlpatterns = router.urls