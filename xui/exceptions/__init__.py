

class AuthenticationFailed(Exception):
    "Raised when authentication to x-ui panel faield"

class InboundDoesNotSupportUID(Exception):
    "Raised when you try to construct a non uid inbound"