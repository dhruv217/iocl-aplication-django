"""
Middleware Module to get current request object from the current thread
"""
from threading import current_thread
from django.utils.deprecation import MiddlewareMixin

REQUESTS = {}

def get_request_obj():
    """
    Function to get the current Request Object
    """
    T = current_thread()
    if T not in REQUESTS:
        return None
    return REQUESTS[T]

class RequestMiddleware(MiddlewareMixin):
    """
    Middleware Class to get request object
    """
    def process_request(self, request):
        """
        Method to check and attach requests to current_thread
        """
        REQUESTS[current_thread()] = request
