from rest_framework.permissions import BasePermission
from datetime import datetime, time

class TimePermission(BasePermission):
    message = "가능한 시간이 아닙니다."
    def has_permission(self, request, view):
        now = datetime.now().time()
        if now >= time(22,0) or now <= time(7,0):
            return False
        return True
    
class UserPermission(BasePermission):
    message = "작성자가 아닙니다."
    def has_object_permission(self, request, view, object):
        if request.method == "GET":
            return True
        elif request.method in ["POST", "PATCH", "DELETE"]:
            if object.user == request.user:
                return True
        else:
            return False
        
class CombinedPermission(TimePermission, UserPermission):
    pass
