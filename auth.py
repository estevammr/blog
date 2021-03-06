from functools import wraps
from flask import request, Response


def check_auth(username, password):
    """Function para verificar se combinacao username /
    password eh valida.
    """
    return username == 'admin' and password == 'secret'


def authenticate():
    """Envia 401 response que habilita autenticacao basica"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
