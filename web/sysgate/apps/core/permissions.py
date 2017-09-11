from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission


def super_o_esta_en_grupo(user, grupo):
    """
    Devuelve `True` si un usuario pertenece a un grupo.
    """

    if not user.is_authenticated():
        return False

    if user.is_superuser:
        return True

    if user.groups.filter(name=grupo).exists():
        return True

    return False


class EsSuperOTienePermisosPorGrupo(BasePermission):
    """
    Se asegura de qu el usuario este en un grupo
    """

    def has_permission(self, request, view):

        grupos_autorizados_mapping = getattr(view, 'grupos_autorizados', {})
        grupos_autorizados = grupos_autorizados_mapping.get(request.method, [])

        return any([super_o_esta_en_grupo(request.user, grupo)
                    for grupo in grupos_autorizados])
