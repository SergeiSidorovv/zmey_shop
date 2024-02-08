from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, "404.html", status=404)


def page_forbidden(request, exception):
    return render(request, "403.html", status=403)


def page_server_error(request):
    return render(request, "500.html", status=500)
