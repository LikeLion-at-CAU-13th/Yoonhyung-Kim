from django.urls import path
from comments.views import *

urlpatterns = [
    path('<int:id>', get_comment_detail), # 추가
]