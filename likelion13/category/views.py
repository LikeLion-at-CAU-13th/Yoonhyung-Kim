from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import *

# Create your views here.

@require_http_methods(["GET"])
def get_category_detail(reqeust, id):
    category = get_object_or_404(Category, pk=id)
    category_detail_json = {
        "id" : category.id,
        "name" : category.name,
    }
    return JsonResponse({
        "status" : 200,
        "data": category_detail_json})