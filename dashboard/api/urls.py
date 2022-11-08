from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (DataViewSet)

router = DefaultRouter()
router.register(r'', DataViewSet, basename='data' )

urlpatterns = [

]
urlpatterns = router.urls
