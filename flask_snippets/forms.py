# you need flask_wtf if you want to use wtf.quickform
from flask_wtf import Form

from wtforms import StringField, validators

# here you are creating a Form Class that you can then create instances of in the view
class TestForm(Form):
    String = StringField('Enter a string here')
    String_validate = StringField('Enter a string that is between 1 and 5 characters', [validators.Length(min=1, max=5)])
