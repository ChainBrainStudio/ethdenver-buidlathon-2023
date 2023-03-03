from flask import Blueprint


blueprint = Blueprint("home", __name__)


@blueprint.route("/")
def index():
    return (
        """<div>
        <a href="http://localhost:3000">UI Home</a></br>
        <a href="http://localhost:5000/api/v1/dashboard">Dashboard</a></br>
        <a href="http://localhost:5000/api/v1/dashboard/1">Dashboard(id:1)</a></br>
        <a href="http://localhost:5000/">Help</a>
        </div>
    """
    )
