

def get_username_from_claim(data):
    """
    This method returns the username from token claims
    """

    return data.get("preferred_username")


def update_user_details(user, claims):
    """
    This method used to update user object with keycloak user id and merchant
    id from token claims
    """

    realm_access = claims.get("realm_access", {})
    roles = realm_access.get("roles", [])

    if "super_admin" in roles:
        user.is_superuser = True
        user.is_staff = True
