from flask.ext.wtf import Form
from wtforms import DateField, IntegerField, SubmitField
from wtforms.validators import NumberRange


class VisitCalculatorForm(Form):
    start_date = DateField('start_date', format='%m/%d/%Y')
    step_size = IntegerField('step_size', [NumberRange(min=1)])
    visit_count = IntegerField('visit_count', [NumberRange(min=1)])
    visit_range = IntegerField('visit_range', [NumberRange(min=0)])
    submit = SubmitField()