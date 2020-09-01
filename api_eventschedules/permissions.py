from rest_framework.permissions import BasePermission

# class IsAuthorOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         message = 'You must be the organizer of this eventschedule.'
#
#         return obj.organizer == request.user
