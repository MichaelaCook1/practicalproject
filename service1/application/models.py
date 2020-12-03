from application import db


#defining database
class attempts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    result = db.Column(db.String(7))
