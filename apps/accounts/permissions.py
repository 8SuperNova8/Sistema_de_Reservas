from rest_framework import permissions

class BaseUserPermission(permissions.BasePermission):
    #Verifica que el usuario este activo
    def has_permission(self, request, view):
        return(
            request.user and
            request.user.is_authenticated and
            request.user.is_active
            )

class IsSuperUser(BaseUserPermission):
    #agregamos un valor adicional
    def has_permission(self, request, view):
        return (super().has_permission(request, view) and 
            request.user.is_superuser)

