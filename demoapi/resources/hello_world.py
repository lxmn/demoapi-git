from flask_restful import Resource


class HelloWorld(Resource):
    def __int__(self, **kwargs):
        self.port = kwargs.get("port")

    def get(self):
        return {"hello": "world"}

