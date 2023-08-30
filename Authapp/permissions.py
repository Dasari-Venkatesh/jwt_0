from rest_framework import permissions

class IsClientUser(permissions.BasePermission):
    # print("i am in isclientuser")
    def has_permission(self, request, view):
        return bool(request.user and request.user.user_type =='Client')


    
class IsAdminUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.user_type=='Admin')
    
    # def has_object_permission(self,request,view,obj):
    #     return request.user==obj