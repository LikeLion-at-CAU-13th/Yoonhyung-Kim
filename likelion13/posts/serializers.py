### Model Serializer case

from rest_framework import serializers
from .models import Post
from .models import Image
from config.custom_api_exceptions import PostConflictException, DailyPostNumLimitException
from datetime import date

class PostSerializer(serializers.ModelSerializer):

  class Meta:
		# 어떤 모델을 시리얼라이즈할 건지
    model = Post
		# 모델에서 어떤 필드를 가져올지
		# 전부 가져오고 싶을 때
    fields = "__all__"

      # 중복된 게시글 제목이 있다면 예외 발생
  def validate(self, data):
    if Post.objects.filter(title=data['title']).exists():
      raise PostConflictException(detail=f"A post with title: '{data['title']}' already exists.")
    
    day = date.today()
    writer = data.get('user')
    if Post.objects.filter(user=writer, created__date = day).exists():
       raise DailyPostNumLimitException("Only one post each day")

    return data

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"