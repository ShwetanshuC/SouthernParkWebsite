from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def calendar_view(request):
    return render(request, "pages/calendar.html")
