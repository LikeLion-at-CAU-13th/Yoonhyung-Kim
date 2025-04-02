from django.urls import path
from category.views import *

urlpatterns = [
    path('<int:id>', get_category_detail),
]