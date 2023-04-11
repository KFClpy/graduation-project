errors = {
    'ExpiredSignatureError': {
        'message': "TokenExpired",
        'code': 66666,
        'data': None,
        'status': 206

    },
    'DecodeError': {
        'message': "TokenInvalid",
        'status': 401
    },
    'NoAuthorizationError': {
        'message': "Missing Authorization",
        'status': 401
    },
    'RevokedTokenError': {
        'message': "Token has been revoked",
        'status': 401
    }

}
