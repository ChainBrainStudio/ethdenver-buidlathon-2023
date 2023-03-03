
from backend.extensions import db



class DashboardService:
    def __init__(self):
        pass

    def save_dashboard_query_result(self, dashboard_query_result):
        db.session.add(dashboard_query_result)
        db.session.commit()
