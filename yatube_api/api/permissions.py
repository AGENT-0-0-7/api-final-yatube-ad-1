from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Аутентифицированным пользователям разрешено всё (POST, PUT, DELETE, GET)
        # Анонимам разрешено только безопасное чтение (GET)
        return (request.method in permissions.SAFE_METHODS or
                request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Читать могут все, изменять/удалять — только автор
        return (request.method in permissions.SAFE_METHODS or
                obj.author == request.user)