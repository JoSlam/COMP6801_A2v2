from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

def index(request):
    name = "joslam"
    return render(request, "index.html", {'name': name})