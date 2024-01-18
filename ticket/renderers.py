from rest_framework import renderers
import json


class UserRenderer(renderers.JSONRenderer):

    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):

        response = ""

        if "ErrorDetail" in str(data):
            response = json.dumps(obj={'errors': data})
        else:
            response = json.dumps(obj=data)

        return response
