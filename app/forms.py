from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    upload = FileField('Image', validators=[FileRequired('Please input an image'), FileAllowed(['jpg', 'png'], 'Only Images')])