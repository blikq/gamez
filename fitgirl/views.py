from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from .scraper import get_data
from .exception import abort


# Create your views here.
def d(r):
    return abort(499)