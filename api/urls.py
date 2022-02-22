from django.urls import path
from api.views import StudentView

urlpatterns = [
    path("student/", StudentView.as_view()),
]
