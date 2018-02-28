from flask_table import Table, Col, LinkCol

class Results(Table):
    buildingName = Col('buildingName', show=False)
    address=Col('address')
    l1=Col('l1')
    l2=Col('l2')
    l3=Col('l3')
    flatno = Col('flatno')
    rent = Col('rent')
    area=Col('area')
   # bathrooms = Col('bathrooms')
    electricity = Col('electricity')
    maintain = Col('maintain')
   