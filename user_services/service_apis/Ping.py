from django.db import connections, OperationalError

from flask_restful import Resource


class Ping(Resource):
    def get(self):
        db_conn = connections["default"]
        try:
            c = db_conn.cursor()
        except OperationalError:
            return "Failed to Connect DB"
        else:
            return "I'm Alive. DB is Available..!!"