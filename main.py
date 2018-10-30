# main.py

from app import app
from db_setup import init_db, db_session
from forms import roomForm,MusicSearchForm
from flask import flash, render_template, request, redirect
from models import Buildings, Room
from tables import Results

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)





@app.route('/new_data', methods=['GET', 'POST'])
def new_data():
    """
    Add a new album
    """
    form = roomForm(request.form)

    if request.method == 'POST' and form.validate():
        # Save the album
        rooms = Room()
        save_changes(rooms, form, new=True)
        flash(' created successfully!')
        return redirect('/')

    return render_template('new_data.html', form=form)

def save_changes(rooms, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    buildings = Buildings()
    buildings.buildingName=form.buildingName.data
    buildings.address=form.address.data
    buildings.l1=form.l1.data
    buildings.l2=form.l2.data
    buildings.l3=form.l3.data

    rooms.buildings = rooms
    rooms.flatno = form.flatno.data
    rooms.rent = form.rent.data
    rooms.area = form.area.data
    #rooms.bathrooms = form.bathrooms.data
    rooms.electricity = form.electricity.data
    rooms.maintain = form.maintain.data

    if new:
        # Add the new album to the database
        db_session.add(rooms)
        db_session.add(buildings)

    # commit the data to the database
    db_session.commit()




if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = True
    app.run(debug=True)
