from django.urls import path
from comments.views import *

urlpatterns = [
    # path('<int:id>/', get_comment_detail), # 추가
    # path('post/<int:post_id>/',comment_list, name='comment_list')

    path('<int:post_id>/', CommentList.as_view()),
    path('<int:post_id>/<int:comment_id>/', CommentDetail.as_view())
]