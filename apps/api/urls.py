# from .views import HealthCheckAPIView
# from django.urls import path,include
# from .views import *

# urlpatterns = [
#     path("api/v1/",include("apps.api.urls"),),
#     path("health/",HealthCheckAPIView.as_view(),name="health",),
# ]

from django.urls import path
from .views import HealthCheckAPIView

urlpatterns = [
    path("health/", HealthCheckAPIView.as_view(), name="health"),
]