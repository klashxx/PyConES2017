from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission


def esta_en_grupo(user, grupo):
    """
    Devuelve `True` si un usuario pertenece a un grupo.
    """

    try:
        return Group.objects.get(
            name=grupo).user_set.filter(id=user.id).exists()
    except ObjectDoesNotExist:
        return False


class EsAdminOTienePermisosPorGrupo(BasePermission):
    """
    Se asegura de qu el usuario este en un grupo
    """

    def has_permission(self, request, view):

        if request.user and request.user.is_superuser:
            return True

        grupos_autorizados_mapping = getattr(view, 'grupos_autorizados', {})
        grupos_autorizados = grupos_autorizados_mapping.get(request.method, [])

        return any([esta_en_grupo(request.user, grupo)
                    for grupo in grupos_autorizados])
