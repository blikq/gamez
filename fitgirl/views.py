from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
# from .scraper import get_data, scrape_from_site, scrape_all_from_site
from .exception import abort
from .models import fitgirl_db
import os

# Create your views here.
def d(request, *args, **kwargs):
    try:
        if request.method == 'GET':
            try:
                # if len(request.headers) == 2:

                # a = scrape_from_site(1,4)
                # fitgirl_db(a)
                return abort(200)
            except Exception:
                return abort(401)
        else:
            return abort(400)
    except Exception:
        return abort(500)