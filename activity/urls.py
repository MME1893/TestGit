from django.urls import path
from .views import ActivityView
from .views import SubCategoryController, MainCategoryController


urlpatterns = [
    path('subcategory/', SubCategoryController.as_view()),
    path('subcategory/<int:user_id>', SubCategoryController.as_view()),
    path('SubCategory/<int:user_id>/<int:main_id>', SubCategoryController.as_view()),
    path("activity/",ActivityView.as_view()),
    path("maincategory/", MainCategoryController.as_view())
]