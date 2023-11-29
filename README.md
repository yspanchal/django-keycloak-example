
# Django Keycloak Example

## Installation

### Using virtualenv
1. Install dependencies: `pip install -r requirements.txt`
2. Update settings.py for following variables,

`OIDC_OP_DISCOVERY_DOCUMENT_URL`

`OIDC_RP_CLIENT_ID`

`OIDC_RP_CLIENT_AUDIENCE`

2. Migrate the database: `python manage.py migrate`
3. Run the server: `python manage.py runserver`
4. open url: http://localhost:8000/admin/
