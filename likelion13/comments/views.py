from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import *

from .serializers import CommentSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

@require_http_methods(["GET"])
def get_comment_detail(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment_detail_json = {
        "id" : comment.id,
        "author" : comment.author,
        "content" : comment.content,
        "created" : comment.created,
        "updated" : comment.updated,
    }
    return JsonResponse({
        "status" : 200,
        "data": comment_detail_json})

#게시물 별로 댓글 조회
@require_http_methods(["GET"])
def comment_list(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    comments = Comment.objects.filter(post=post)
    comment_json_all = []

    for comment in comments:
        comment_json = {
            "id": comment.id,
            "post": comment.post.id,
            "author": comment.author,
            "content": comment.content,
        }
        comment_json_all.append(comment_json)

    return JsonResponse({
            'status': 200,
            'message': '게시글 목록 조회 성공',
            'data': comment_json_all
        })

class CommentList(APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class CommentDetail(APIView):
    def get(self, request, post_id,comment_id):
        post = get_object_or_404(Post, id=post_id)
        comment = get_object_or_404(Comment, pk = comment_id, post=post)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    def delete(self,request,post_id,comment_id):
        post = get_object_or_404(Post, id=post_id)
        comment = get_object_or_404(Comment, pk = comment_id, post=post)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)