from database import db

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    hasDiet = db.Column(db.Boolean, nullable=False)
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "date": str(self.date),
            "hasDiet": self.hasDiet 
        }