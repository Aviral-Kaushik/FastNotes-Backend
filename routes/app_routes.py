from fastapi import APIRouter
from models.note import Note
from config.mongo_db import conn
from schemas.note import *
from bson import ObjectId
from fastapi import HTTPException

app_routes = APIRouter()

@app_routes.post("/note")
async def add_note(note: Note): 
    inserted = conn.fastNotes.notes.insert_one(dict(note))
    inserted_note = conn.fastNotes.notes.find_one({"_id": inserted.inserted_id})
    return note_entity(inserted_note)

@app_routes.get("/note")
async def get_note(note_id: str):
    # ✅ Handle invalid ObjectId format
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID format")
    
    note: Note = conn.fastNotes.notes.find_one({"_id": ObjectId(note_id)})

    # ✅ Handle not found
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return note_entity(note)

@app_routes.get("/notes")
async def get_all_notes():
    notes = conn.fastNotes.notes.find()
    
    return notes_entity(notes)

@app_routes.patch("/note")
async def update_note(note_id: str, note: Note):
     # ✅ Handle invalid ObjectId format
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID format")
    
    result = conn.fastNotes.notes.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": dict(note)}
    )
    
    if result.matched_count == 0:
         raise HTTPException(status_code=404, detail="Invalid note ID.")
    
    updated_note = conn.fastNotes.notes.find_one({"_id": ObjectId(note_id)})

    return note_entity(updated_note)

@app_routes.delete("/note")
async def delete_note(note_id: str):
    # ✅ Handle invalid ObjectId format
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID format")
    
    deleteNote = conn.fastNotes.notes.delete_one({"_id": ObjectId(note_id)})

    if deleteNote.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Invalid note ID.")
    
    return {"message": "Note deleted successfully"}