from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse


class AuthRequiredMiddleware:
    """
    Middleware to ensure that only authenticated users can access most pages,
    while redirecting authenticated users away from the login page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URL patterns that are exempt from login required check
        # Change 'login' to your actual login view name
        login_url = reverse('auth.login')
        exempt_urls = [login_url]

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Redirect authenticated users away from the login page
            if request.path == login_url:
                # Redirect to the default post-login page
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            # Redirect unauthenticated users to the login page if they're trying to access a protected URL
            if request.path not in exempt_urls:
                return redirect(login_url)

        response = self.get_response(request)
        return response
