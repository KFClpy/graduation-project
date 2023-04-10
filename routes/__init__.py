from routes.admin import admin_route
from routes.super import super_route
from routes.user import user_route

routes={
    "admin":admin_route,
    "super":super_route,
    "user":user_route
}