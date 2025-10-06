from fastapi import FastAPI, HTTPException, Path
from typing import Dict, List, Optional

try:
    from pydantic import RootModel

    class GenericItem(RootModel[Dict[str, str]]):
        pass

    def get_root(item):
        return item.root

except ImportError:
    from pydantic import BaseModel

    class GenericItem(BaseModel):
        __root__: Dict[str, str]

    def get_root(item):
        return item.__root__

app = FastAPI()

# Lista "database" temporaneo
items: List[Dict] = []

# POST -> aggiungo un nuovo item
@app.post("/items")
def add_item(item: GenericItem):
    data = get_root(item)
    items.append(data)
    return {"message": "Item aggiunto con successo", "item": data}

# GET -> restituisce tutti gli item
@app.get("/items")
def get_items():
    return {"items": items}

# PATCH-like -> aggiorna solo i campi forniti, identifica tramite ID
@app.put("/items/{item_id}")
def update_item(
    item_id: str = Path(..., description="ID dell'item da aggiornare"),
    item: GenericItem = None
):
    data = get_root(item)
    for existing_item in items:
        if existing_item.get("ID") == item_id:
            # Aggiorna solo i campi forniti
            existing_item.update(data)
            return {"message": f"Item {item_id} aggiornato con successo", "item": existing_item}
    
    raise HTTPException(status_code=404, detail=f"Item con ID {item_id} non trovato")
