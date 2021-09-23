from flask import render_template, request, redirect
from app import app 
from models.event_list import *
from models.event import *

@app.route("/events")
def index():
    return render_template("index.html", title="Home", events = events)

@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["Date"]
    event_name_event = request.form["Event_name"]
    event_guest_number = request.form["number_of_guests"]
    event_room_location = request.form["room_location"]
    event_desc = request.form["description"]
    new_event = Event(event_date, event_name_event, event_guest_number, event_room_location, event_desc, False)
    add_new_event(new_event)
    return render_template("index.html", title="Home", events = events)

    


@app.route("/events/delete/<index>")
def delete_event(index):
    event = events[int(index)]
    event_to_delete(event)
    return redirect("/events")
    # return index()
