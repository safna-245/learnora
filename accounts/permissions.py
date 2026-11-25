from rest_framework.permissions import BasePermission

class IsTrainerUser(BasePermission):

    def has_permission(self, request, view):

        if request.user.role =="trainer":

            return True

        else:

            return False