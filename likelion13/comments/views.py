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