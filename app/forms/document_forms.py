from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class DocumentUploadForm(FlaskForm):
    """Document upload form"""
    title = StringField('Document Title', validators=[
        DataRequired(),
        Length(min=3, max=100)
    ])
    document = FileField('Upload Document', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'docx', 'doc'], 'Only PDF and Word documents are allowed!')
    ])
    course_id = SelectField('Course (Optional)', 
                        validators=[Optional()],
                        coerce=int)
    submit = SubmitField('Upload')

class QuestionGenerationForm(FlaskForm):
    """Question generation form based on UBTEB exam template"""
    # Exam header information
    exam_series = StringField('Exam Series', validators=[DataRequired()], 
                             default='JULY 2023')
    programme_list = StringField('Programme List', validators=[DataRequired()], 
                                default='DIPLOMA IN INFORMATION TECHNOLOGY')
    paper_name = StringField('Paper Name', validators=[DataRequired()], 
                            default='DATABASE SYSTEMS')
    paper_code = StringField('Paper Code', validators=[DataRequired()], 
                            default='DIT 014')
    year_semester = StringField('Year and Semester', validators=[DataRequired()], 
                              default='YEAR II SEMESTER I')
    exam_date = DateField('Exam Date', validators=[DataRequired()], 
                         format='%Y-%m-%d')
    
    # Question generation settings
    difficulty = SelectField('Difficulty Level', validators=[
        DataRequired()
    ], choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('mixed', 'Mixed')
    ], default='medium')
    
    submit = SubmitField('Generate Questions') 