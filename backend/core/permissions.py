from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(
            name="ADMIN"
        ).exists()


class IsSales(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(
            name="SALES"
        ).exists()


class IsFinance(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(
            name="FINANCE"
        ).exists()


class IsTechnician(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(
            name="TECHNICIAN"
        ).exists()


class IsManagement(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(
            name="MANAGEMENT"
        ).exists()
