from django.views.generic import RedirectView
from django.urls import reverse
from django.utils.http import urlencode
from oauth2_authcodeflow.conf import constants as oidc_constants


class AdminRedirectView(RedirectView):
    def get_url(self):
        """
        Generate url for oidc redirect
        """
        oidc_urlname = oidc_constants.OIDC_URL_AUTHENTICATION_NAME
        oidc_url = reverse(oidc_urlname)
        next = self.request.GET.get("next")
        if not next:
            next = reverse("admin:index")
        fail = reverse("echo")
        return f"{oidc_url}?next={next}&fail={fail}"


class DjangoAdminLoginView(AdminRedirectView):
    """
    Custom django admin login view to redirect to Oidc provider
    """

    def get_redirect_url(self, *args, **kwargs):
        """
        If user is not authenticated redirect to Oidc provider login else
        check for permissions
        """
        if self.request.user.is_authenticated:
            if not (self.request.user.is_superuser and self.request.user.is_staff):
                msg = f"You are authenticated as {self.request.user.username}, but are not authorized to access this page."
                url = reverse("echo")
                return f"{url}?error={msg}"

        return self.get_url()


class DjangoAdminLogoutView(AdminRedirectView):
    """
    Custom django admin logout view to redirect to Oidc provider
    """

    def get_redirect_url(self, *args, **kwargs):
        """
        If user is authenticated redirect to Oidc provider login else
        redirect to Oidc provider login
        """
        if self.request.user.is_authenticated:
            print("self.get_url() -- ", self.get_url())
            params = urlencode(
                {
                    "next": self.get_url(),
                    "fail": reverse("echo"),
                }
            )
            url = f"{reverse(oidc_constants.OIDC_URL_TOTAL_LOGOUT_NAME)}?{params}"
            return url

        return self.get_url()
