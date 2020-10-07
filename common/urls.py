from django.urls import path

from .views import DatetimeView, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', DatetimeView.as_view()),
]
