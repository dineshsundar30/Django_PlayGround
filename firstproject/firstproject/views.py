from django.shortcuts import render

def pag_not_found(request, exception):
    return render(request, "404.html", status=404)
