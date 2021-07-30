from django.conf.urls import url
from django.urls import path, include

from .views import (
ClosePairsListApiView,
)

urlpatterns =[
  path('', ClosePairsListApiView.as_view()),
]