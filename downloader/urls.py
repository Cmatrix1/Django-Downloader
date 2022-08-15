from django.urls import path
from .views import DownladPageView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:id>", DownladPageView.as_view(), name="test"),
]
