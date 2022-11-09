from django.shortcuts import render


def custom_page_not_found_view(request, exception):
    return render(request, "basis_of_project/errors/404.html", {})

#
# def custom_error_view(request, exception=None):
#     return render(request, "/basis_of_project/errors/500.html", {})
#
#
# def custom_permission_denied_view(request, exception=None):
#     return render(request, "basis_of_project/errors/403.html", {})
#
#
# def custom_bad_request_view(request, exception=None):
#     return render(request, "basis_of_project/errors/400.html", {})

#
# def handler404(request, exception):
#     context = {}
#     response = render(request, "pages/errors/404.html", context=context)
#     response.status_code = 404
#     return response
# def handler500(request):
#     context = {}
#     response = render(request, "pages/errors/500.html", context=context)
#     response.status_code = 500
#     return response
