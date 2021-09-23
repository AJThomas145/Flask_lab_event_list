from models.event import *

event1 = Event("23-09-2021", "Music Festival", 100, "room 1", "rock", True)
event2 = Event("23-10-2021", "Dance Festival", 200, "room 2", "Country dancing", True)
event3 = Event("23-11-2021", "Book Festival", 50, "room 3", "books", False)
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)

def event_to_delete(event):
    events.remove(event)