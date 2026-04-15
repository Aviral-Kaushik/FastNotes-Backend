from fastapi import APIRouter
from models.note import Note
from config.mongo_db import conn
from schemas.note import *

app_routes = APIRouter()

@app_routes.post("/note")
async def add_note(note: Note): 
    print(note)
    inserted = conn.fastNotes.notes.insert_one(dict(note))
    inserted_note = conn.fastNotes.notes.find_one({"_id": inserted.inserted_id})
    print(inserted_note)
    print(note_entity(inserted_note))
    return note_entity(inserted_note)