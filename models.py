from app import db


class Buildings(db.Model):
    __tablename__ = "buildings"

   
    buildingName = db.Column(db.String,primary_key=True)
    address=db.Column(db.String)
    l1=db.Column(db.String)
    l2=db.Column(db.String)
    l3=db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)


class Room(db.Model):
    """"""
    __tablename__ = "rooms"

    flatno = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)
    area = db.Column(db.Integer)
   # bathrooms = db.Column(db.Integer)
    electricity = db.Column(db.String)
    maintain = db.Column(db.String)
    