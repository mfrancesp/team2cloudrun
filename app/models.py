from app import db

class dates(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tittle = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)
    extend_existing=True