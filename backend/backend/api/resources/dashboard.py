from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from backend.api.schemas import UserSchema
from backend.models import DashboardQueryResult
from backend.extensions import db
from backend.commons.pagination import paginate
from backend.controllers.api.v1 import APIV1Controller

DEFAULT_INPUT = "What proposal has the most votes?"
DEFAULT_SUBGRAPH = "aave-governance"

class DashboardCreator(Resource):
    """Dashboard Resource
    """
    # to enable security uncomment line below
    # method_decorators = [jwt_required()]


    def post(self):
        try:
            input_sentence = request.get_json().get("input")
            if input_sentence == "":
                raise
        except:
            input_sentence = DEFAULT_INPUT

        try:
            subgraph = request.get_json().get("subgraph")
            if subgraph == "":
                raise
        except:
            subgraph = DEFAULT_SUBGRAPH

        print("=========== input_sentence ===============")
        print(input_sentence)
        print("=========== subgraph ===============")
        print(subgraph)
        controller = APIV1Controller()
        response = controller.handle_query_for_dashboard(input_sentence, subgraph)
        print(response)
        return response




class DashboardViewer(Resource):
    """DashboardViewer Resource
    """
    # to enable security uncomment line below
    # method_decorators = [jwt_required()]


    def get(self, dashboard_id):
        return APIV1Controller().get_dashboard(dashboard_id)
