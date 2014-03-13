from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField,IntegerField
from wtforms.fields.html5 import DateField
import datetime

from wtforms.validators import Required

class BlahForm(Form):
    text_entry = TextField('text_entry', validators = [Required()],default='default text')
    boolean_entry = BooleanField('boolean_entry', default = False)
    date_entry = DateField('date_entry',default=datetime.date.today())
    select_entry = SelectField('select_entry', choices=[('value1', 'label1'), ('value2', 'label2'), ('value3', 'label3')],default='value2')
    integer_entry = IntegerField('integer_entry',default=7)
    
