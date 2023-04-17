from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField
from flask_ckeditor import CKEditorField


class EditForm(FlaskForm):
    career_name = StringField('Career Name')
    description = StringField("Description")
    content = CKEditorField('Content')
    image = FileField('Upload Image')
    submit =SubmitField('Save changes')