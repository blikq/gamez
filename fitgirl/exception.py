from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse, HttpResponseNotFound, JsonResponse
import json


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

class HttpResaponseClientClosedRequest(HttpResponse):
    status_code = 499

class HttpResponseRequestedRangeNotSatisfiable(HttpResponse):
    status_code = 416

class HttpResponseGone(HttpResponse):
    status_code = 410

class HttpResponseConflict(HttpResponse):
    status_code = 409

class HttpResponseTooManyRequests(HttpResponse):
    status_code = 429

class HttpResponseMethodNotAllowed(HttpResponse):
    status_code = 405

class HttpResponseLengthRequired(HttpResponse):
    status_code = 411

class HttpResponsePreconditionFailed(HttpResponse):
    status_code = 412

class HttpResponsePayloadTooLarge(HttpResponse):
    status_code = 413

def abort(status_code: int, msg=None):
    if status_code == 200:
        if msg is not None:
            json_ = {
                "success": True,
                "Status": 200,
            }
            json_ = json.dumps(json_)
            return JsonResponse(json_)
        elif msg == None:
            json_ = {
                "success": True,
                "Status": 200,
                "message": msg
            }
            json_ = json.dumps(json_)
            return JsonResponse(json_)

    elif status_code == 400:
        json_ = {
            "success": False,
            "status_code": 400,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "Invalid request",
                        "message": "Bad Request",
                    }
                ],
                "code": 401,
                "message": "Bad Request",
            }
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
            "sucess": False,
            "status_code": 404,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "notFound",
                        "message": "Either there is no API method associated with the URL path of the request, or the request refers to one or more resources that were not found."
                    }
                ],
                "code": 404,
                "message": "Not Found"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseNotFound(json_, content_type="application/json")
    elif status_code == 405:
        json_ = {
            "success": False,
            "status_code": 405,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "methodNotAllowed",
                        "message": "The HTTP verb is not supported by the URL endpoint used in the request. This can happen, for example, when using the wrong verb with the /upload or /download URLs."
                    }
                ],
                "code": 405,
                "message": "Invalid method request"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseMethodNotAllowed(json_, content_type='application/json')
    elif status_code == 408:
        json_ = {
            "success": False,
            "status_code": 408,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "uploadBrokenConnection",
                        "message": "The request timed out. Please try again using truncated exponential backoff.",
                    }
                ],
                "code": 408,
                "message": "request timed out",
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseConflict(json_, content_type='application/json')

    elif status_code == 409:
        json_ = {
            "success": False,
            "status_code": 409,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "conflict",
                        "message": "You already own this bucket. Please select another name."
                    }
                ],
                "code": 409,
                "message": "You already own this bucket. Please select another name."
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseConflict(json_, content_type='application/json')
    elif status_code == 410:
        json_ = {
            "success": False,
            "status_code": 410,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "Gone",
                        "message": "You have attempted to use a resumable upload session or rewrite token that is no longer available. If the reported status code was not successful and you still wish to complete the upload or rewrite, you must start a new session."
                    }
                ],
                "code": 410,
                "message": "You have attempted to use a resumable upload session or rewrite token that is no longer available. If the reported status code was not successful and you still wish to complete the upload or rewrite, you must start a new session."
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseGone(json_, content_type='application/json')
    elif status_code == 411:
        json_ = {
            "success": False,
            "status_code": 411,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "Length Required",
                        "message": "You must provide the Content-Length HTTP header. This error has no response body."
                    }
                ],
                "code": 411,
                "message": "Length Required"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseLengthRequired(json_, content_type='application/json')
    elif status_code == 412:
        json_ = {
            "success": False,
            "status_code": 412,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "Precondition Failed",
                        "message": "At least one of the pre-conditions you specified did not hold."
                    }
                ],
                "code": 412,
                "message": "conditionNotMet"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponsePreconditionFailed(json_, content_type='application/json')
    elif status_code == 413:
        json_ = {
            "success": False,
            "status_code": 413,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "uploadTooLarge",
                        "message": "Attempt to upload an object that is too large."
                    }
                ],
                "code": 413,
                "message": "Attempt to upload an object that is too large"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponsePayloadTooLarge(json_, content_type='application/json')
    
    elif status_code == 416:
        json_ = {
            "success": False,
            "status_code": 416,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "Requested Range Not Satisfiable",
                        "message": "The requested Range cannot be satisfied."
                    }
                ],
                "code": 416,
                "message": "Requested Range Not Satisfiable"
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseRequestedRangeNotSatisfiable(json_, content_type='application/json')
    elif status_code == 429:
        json_ = {
            "success": False,
            "status_code": 429,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "Too Many Requests",
                        "message": "A Cloud Storage JSON API usage limit was exceeded. If your application tries to use more than its limit, additional requests will fail. Throttle your client's requests, and/or use truncated exponential backoff."
                    }
                ],
                "code": 429,
                "message": "A Cloud Storage JSON API usage limit was exceeded. If your application tries to use more than its limit, additional requests will fail. Throttle your client's requests, and/or use truncated exponential backoff."
            }
        }
        json_ = json.dumps(json_)
        return HttpResponseTooManyRequests(json_, content_type='application/json')
    elif status_code == 499:
        json_ = {
            "success": False,
            "status_code": 499,
            "error": {
                "errors": [
                    {
                        "domain": "global",
                        "reason": "Client Closed Request",
                        "message": "The resumable upload was cancelled at the client's request prior to completion. This error has no response body."
                    }
                ],
                "code": 499,
                "message": "The resumable upload was cancelled at the client's request prior to completion. This error has no response body."
            }
        }
        json_ = json.dumps(json_)
        return HttpResaponseClientClosedRequest(json_, content_type='application/json')