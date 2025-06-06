from datetime import datetime
from app import db

class Document(db.Model):
    """Document model for storing uploaded documents"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.id'), nullable=True)
    
    # Relationships
    questions = db.relationship('Question', backref='document', lazy=True, cascade="all, delete-orphan")
    question_sets = db.relationship('QuestionSet', backref='document', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Document('{self.title}', '{self.filename}')"