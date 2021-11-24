from django.urls import path

from trims.views import (
    TrimView,
    TrimPathView
)

urlpatterns = [
    path('', TrimView.as_view()),
    path('/<int:trim_id>', TrimPathView.as_view())
]
