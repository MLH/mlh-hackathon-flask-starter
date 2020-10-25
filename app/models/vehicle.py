from app.extensions import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer(), primary_key=True)
    vehicle_type = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, id, vehicle_type):
        self.id = id
        self.vehicle_type = vehicle_type

    @staticmethod
    def find_or_create_from_token():

        """Find existing user or create new User instance"""
        instance = Vehicle.query.filter_by(vehicle_type='scooter').first()

        if not instance:
            instance = Vehicle('x', 'y')
            db.session.add(instance)
            db.session.commit()

        return instance

    def __repr__(self):
        return "<User: {}>".format(self.id)
