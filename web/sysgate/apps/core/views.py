from django.shortcuts import render
from django.views.defaults import (bad_request, page_not_found,
                                   permission_denied, server_error)
from django.views.generic import View


def error_400(request, exception):
    return bad_request(request, exception)


def error_403(request, exception):
    return permission_denied(request, exception)


def error_404(request, exception):
    return page_not_found(request, exception)


def error_500(request):
    return server_error(request)

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html')
