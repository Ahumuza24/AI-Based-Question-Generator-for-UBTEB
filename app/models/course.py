from datetime import datetime
from app import db

class Course(db.Model):
    """Course model for organizing papers within a program"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)
    
    # Relationships
    papers = db.relationship('Paper', backref='course', lazy=True, cascade="all, delete-orphan")
    documents = db.relationship('Document', backref='course', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Course('{self.name}')"