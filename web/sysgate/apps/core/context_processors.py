from django.conf import settings
from django.core.urlresolvers import resolve


def breadcrumbs(request):

    apps = {
        'account': {'login': 'Autenticación',
                    'contacto': 'Contáctenos',
                    'profile': 'Mi Cuenta',
                    'registro': 'Registro',},
        'metrics': {'metrics': 'Métricas',},
    }

    try:
        app_name = request.resolver_match.app_name
    except AttributeError:
        app_name = None

    sep = '/'
    breads = []
    full_path = '/'
    paths = request.path_info.split('/')

    del paths[0]
    if paths[-1]:
        last_sep = ''
    else:
        last_sep = sep
        del paths[-1]

    for i, path in enumerate(paths):
        if i == len(paths) - 1:
            sep = last_sep

        full_path = '{0}{1}{2}'.format(full_path, path, sep)
        try:
            resolve(full_path).url_name
        except:
            continue

        try:
            verbose_path = apps[app_name][path]
        except:
            verbose_path = path

        breads.append({'path': verbose_path, 'full_path': full_path})

    return {'breads': breads}
