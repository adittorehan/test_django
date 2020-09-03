from django.http import HttpResponse


def index(reqeust):
    return HttpResponse("Hello Aditto Rehan")
