def note_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": str(item["title"]),
        "desc": str(item["desc"]),
        "important": bool(item["important"])  
    }

def notes_entity(items) -> list:
    return [note_entity(item) for item in items]