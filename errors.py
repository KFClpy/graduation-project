errors = {
    'ExpiredSignatureError': {
        'message': "TokenExpired",
        'status': 401
    },
    'DecodeError': {
        'message': "TokenInvalid",
        'status': 401
    },
    'NoAuthorizationError':{
        'message':"Missing Authorization",
        'status':401
    },
    'RevokedTokenError':{
        'message':"Token has been revoked",
        'status':401
    }

}