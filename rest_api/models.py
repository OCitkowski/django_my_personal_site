from django.db import models
from rest_framework import authentication


class BearerAuthentication(authentication.TokenAuthentication):

    # https://stackoverflow.com/questions/45737363/what-is-purpose-of-changing-token-key-name-in-djangorestframework
    # Simple token based authentication using utvsapitoken.
    #
    # Clients should authenticate by passing the token key in the 'Authorization'
    # HTTP header, prepended with the string 'Bearer '.  For example:
    #
    # Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812

    keyword = 'Bearer'
