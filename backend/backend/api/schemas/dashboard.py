from backend.models import DashboardQueryResult
from backend.extensions import ma, db


class UserSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    password = ma.String(load_only=True, required=True)

    class Meta:
        model = DashboardQueryResult
        sqla_session = db.session
        load_instance = True
        exclude = ("_password",)
