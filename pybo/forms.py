from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from pybo.models import remains



class AmountForm(FlaskForm):
    content = TextAreaField('수량', validators=[DataRequired('수량은 필수입력 항목입니다.')])
