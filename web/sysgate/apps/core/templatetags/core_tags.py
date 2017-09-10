from django import template


register = template.Library()


@register.filter('en_grupo')
def en_grupo(user, group_name):
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False


@register.filter('sin_grupos')
def sin_grupos(user):
    groups = user.groups.all().values_list('name', flat=True)
    return True if not len(groups) else False
