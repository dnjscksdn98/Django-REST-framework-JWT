# Django Project with JWT Authentication

## Install dependencies

<pre>
<code>
pip install django-rest-auth
pip install djangorestframework-jwt
</code>
</pre>

## Setups

<pre>
<code>
INSTALLED_APPS = [
    //
    'rest_framework.authtoken',
    'rest_auth',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

REST_USE_JWT = True
</code>
</pre>
