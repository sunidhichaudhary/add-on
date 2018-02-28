# forms.py

from wtforms import Form, StringField, SelectField, validators

class MusicSearchForm(Form):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')


class roomForm(Form):
    
    buildingName = StringField('name')
    address = StringField('address')
    l1 = StringField('l1')
    l2 = StringField('l2')
    l3 = StringField('l3')
    flatno=StringField('flatno')
    rent=StringField('rent')
    area=StringField('area')
   # bathrooms=StringField('bathrooms')
    electricity=StringField('electricity')
    maintain=StringField('maintain')
   
