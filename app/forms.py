from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField,IntegerField
from wtforms.fields.html5 import DateTimeField
import datetime

from wtforms.validators import Required

class BlahForm(Form):
    text_entry = TextField('text_entry', validators = [Required()],default='default text')
    boolean_entry = BooleanField('boolean_entry', default = False)
    datetime_entry = DateTimeField('datetime_entry',default=datetime.datetime.utcnow())
    select_entry = SelectField('select_entry', choices=[('value1', 'label1'), ('value2', 'label2'), ('value3', 'label3')],default='value2')
    integer_entry = IntegerField('integer_entry',default=7)
    
