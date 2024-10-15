import jwt
from django.http import HttpResponse, JsonResponse
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request information before the view is called
        logger.info(f"{now()} - {request.method} request to {request.path}")

        # Call the view
        response = self.get_response(request)

        # Log response information after the view is called
        logger.info(f"{now()} - Response status: {response.status_code}")

        return response


class ExceptionHandlingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            return HttpResponse(f"Error occurred :: {str(e)}", status=500)
        return response


class CustomAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for token in header
        token = request.headers.get('X-Custome-Token')
        if not token or token != 'my-token':
            return HttpResponse("Unauthorized", status=401)

        # If token is valid, continue processing the request
        response = self.get_response(request)
        return response


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # get the token
        token = self.get_jwt_token(request)
        print("\n\n")
        print(token)
        print("\n\n")
        if token:
            try:
                # decode token
                payload = jwt.decode(token, "my-jwt-secret-key", algorithms=['HS256'])
                print("\n\n\n")
                print("payload :: ", payload)
                print("\n\n\n")
                request.user = payload
            except (ExpiredSignatureError, DecodeError, InvalidTokenError):
                return JsonResponse({"error": "Invalid or expired token"}, status=401)

        # If no token is provided, continue the request
        return self.get_response(request)

    def get_jwt_token(self, request):
        # extract JWT token from auth
        auth_head = request.headers.get('Authorization')
        if auth_head and auth_head.startswith('Bearer '):
            print("\n\n\n\n")
            print("auth_head ::", auth_head)
            print("\n\n\n\n")
            return auth_head.split(" ")[1]
        return None
