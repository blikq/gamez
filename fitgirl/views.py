from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from .scraper import get_data, scrape_from_site
from .exception import abort
from .models import fitgirl_db


# Create your views here.
def d(r):
    try:
        a = scrape_from_site(1,4)
        fitgirl_db(a)
        return abort(200)
    except Exception:
        return abort(401)