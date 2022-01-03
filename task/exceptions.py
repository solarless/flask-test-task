from werkzeug.exceptions import HTTPException


class PermissionDenied(HTTPException):
    code = 403
