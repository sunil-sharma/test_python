from app import db
from sqlalchemy.dialects.postgresql import JSON


class ContentItem(db.Model):
    __tablename__ = 'content_items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.Text())
    
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<id {}>'.format(self.id)