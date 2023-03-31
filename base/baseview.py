from flask import jsonify, request
from flask.views import MethodView


class BaseView(MethodView):
    def __init__(self, *args, **kwargs):
        self.__setattr__('request', request)
        super(BaseView, self).__init__(*args, **kwargs)

    def formattingData(self, code, msg, data):
        return jsonify(
            {
                "code": code,
                "message": msg,
                "data": data
            }
        )
