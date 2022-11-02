from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse, HttpResponseNotFound
import json


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401


def abort(status_code):
    if status_code == 400:
        json_ = {
            "success": False,
            "status_code": 400,
            "message": "Bad request"
        }
        json_ = json.dumps(json_)
        return HttpResponseBadRequest(json_, content_type='application/json')

    elif status_code == 401:
        json_ = {
            "success": False,
            "status_code": 401,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "required",
                        "message": "Login Required",
                        "locationType": "header",
                        "location": "Authorization"
                    }
                ],
                "code": 401,
                "message": "Login Required"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseUnauthorized(json_, content_type='application/json')

    elif status_code == 403:
        json_ = {
            "success": False,
            "status_code": 403,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "forbidden",
                        "message": "Forbidden"
                    }
                ],
                "code": 403,
                "message": "Forbidden"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseForbidden(json_, content_type="application/json")
    elif status_code == 404:
        json_ = {
            "sucess": True,
            "status_code": 404,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "notFound",
                        "message": "Not Found"
                    }
                ],
                "code": 404,
                "message": "Not Found"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseNotFound(json_, content_type="application/json")
        # return HttpResponse(json_, conrtent_type="application/json", status_code=404)

