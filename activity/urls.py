from django.urls import path
from .views import SubCategory, ActivityView


urlpatterns = [
    path('SubCategory/<int:user_id>/<int:main_id>', SubCategory.as_view()),
    path('activity', ActivityView.as_view())
]