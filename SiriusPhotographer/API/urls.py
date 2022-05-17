from rest_framework import routers
from .api import RestViewSet

router = routers.DefaultRouter()
router.register('api/rest', RestViewSet, 'rest')

urlpatterns = router.urls