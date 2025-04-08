from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import *

# Create your views here.

@require_http_methods(["GET"])
def get_comment_detail(reqeust, id):
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
    post = get_object_or_404(Comment,pk=post_id)
    comment_all = Comment.objects.all()
    comment_json_all = []

    for comment in comment_all:
        comment_json = {
            "id": comment.id,
            "post": comment.post.id,
            "author": comment.author,
            "content": comment.content,
        }
        if post_id == comment.post.id:
            comment_json_all.append(comment_json)

    return JsonResponse({
            'status': 200,
            'message': '게시글 목록 조회 성공',
            'data': comment_json_all
        })