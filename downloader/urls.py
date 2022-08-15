from django.urls import path
from .views import DownladPageView, FileDownloadView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:id>", DownladPageView.as_view(), name="test"),
    path('download/<int:id>/',FileDownloadView.as_view())
]
