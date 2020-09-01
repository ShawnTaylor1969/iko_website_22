from rest_framework.permissions import BasePermission

# class IsAuthorOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         message = 'You must be the author of this timeline.'
#
#         return obj.author == request.user
