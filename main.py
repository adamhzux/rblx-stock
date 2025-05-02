from typing import Union
from roblox import Client
from fastapi import FastAPI
import warnings
import os
# suppress RuntimeWarning
warnings.filterwarnings('ignore', category=RuntimeWarning)

app = FastAPI()
client = Client(os.environ.get("TOKEN"))

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{place_id}")
async def read_item(place_id: int):
    place = await client.get_place(place_id)  # Await the coroutine first
    universe = place.universe                 # Now this should be accessible

    # If you want playing count, fetch the full universe object
    full_universe = await client.get_universe(universe.id)
    return  full_universe.playing


#py -m uvicorn rblx-stock:app --reload to run
