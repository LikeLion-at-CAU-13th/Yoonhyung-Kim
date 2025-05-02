from django.urls import path
from posts.views import *

urlpatterns = [
	#path("", hello_world, name="hello_world"),
    #path("page", index, name="my-page"),
    #path('<int:id>', get_post_detail),
 	
    # path('', post_list, name="post_list"),
    # path('<int:post_id>/', post_detail, name='post_detail'), # Post 단일 조회
    # path('category/<int:category_id>/',post_list_by_category, name='post_list_by_category'),
    # path('logtest/', test_log_view),

    path('', PostList.as_view()), # post 전체 조회
    path('<int:post_id>/', PostDetail.as_view()) # post 개별 조회
]